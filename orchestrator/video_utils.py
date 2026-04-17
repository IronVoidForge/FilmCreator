from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .common import ensure_dir


class VideoFrameExtractionError(RuntimeError):
    """Raised when a video frame could not be extracted by any available backend."""


def extract_last_frame(video_path: Path, output_path: Path) -> Path:
    video_path = video_path.resolve()
    output_path = output_path.resolve()
    ensure_dir(output_path.parent)

    attempts: list[tuple[str, callable]] = [
        ("imageio", lambda: _extract_with_imageio(video_path, output_path)),
        ("opencv", lambda: _extract_with_opencv(video_path, output_path)),
        ("ffmpeg", lambda: _extract_with_ffmpeg(video_path, output_path)),
    ]

    errors: list[str] = []
    for backend, extractor in attempts:
        try:
            extractor()
            if output_path.exists():
                return output_path
        except Exception as exc:  # pragma: no cover - backend availability is environment-specific
            errors.append(f"{backend}: {exc}")

    error_text = "; ".join(errors) if errors else "no extraction backends were available"
    raise VideoFrameExtractionError(f"Could not extract the last frame from {video_path}: {error_text}")


def _extract_with_imageio(video_path: Path, output_path: Path) -> None:
    import imageio.v3 as iio
    from PIL import Image

    last_frame = None
    for frame in iio.imiter(video_path):
        last_frame = frame
    if last_frame is None:
        raise VideoFrameExtractionError("video contains no readable frames")

    Image.fromarray(last_frame).save(output_path)


def _extract_with_opencv(video_path: Path, output_path: Path) -> None:
    import cv2

    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise VideoFrameExtractionError("OpenCV could not open the video")

    try:
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        if frame_count > 0:
            capture.set(cv2.CAP_PROP_POS_FRAMES, max(frame_count - 1, 0))

        ok, frame = capture.read()
        if not ok or frame is None:
            capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok = False
            while True:
                next_ok, next_frame = capture.read()
                if not next_ok or next_frame is None:
                    break
                ok = True
                frame = next_frame

        if not ok or frame is None:
            raise VideoFrameExtractionError("OpenCV could not decode any frames")

        if not cv2.imwrite(str(output_path), frame):
            raise VideoFrameExtractionError("OpenCV failed to write the extracted frame")
    finally:
        capture.release()


def _extract_with_ffmpeg(video_path: Path, output_path: Path) -> None:
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        raise VideoFrameExtractionError("ffmpeg executable was not found on PATH")

    command = [
        ffmpeg_path,
        "-y",
        "-sseof",
        "-0.1",
        "-i",
        str(video_path),
        "-update",
        "1",
        "-frames:v",
        "1",
        str(output_path),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        stderr = (completed.stderr or "").strip()
        raise VideoFrameExtractionError(stderr or f"ffmpeg exited with status {completed.returncode}")

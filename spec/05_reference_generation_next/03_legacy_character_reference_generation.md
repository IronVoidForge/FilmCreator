Status: 75% (partly outdated)

# 2.1 Character Reference Generation

## Goal

Generate reusable character references at the project scope before downstream scene, shot, and keyframe composition depends on them.

The generation path should be staged:

1. text-to-image portrait or bust
2. image-to-image full-body using the approved portrait as the identity source
3. image-to-image supporting views using the approved full-body or portrait as the source

## Inputs

- Character bible and descriptor artifacts
- Character prompt bundle in `03_prompt_packages/prepared/characters/<name>/`
- Review and approval metadata
- Local generation workflow suitable for text-to-image and image-to-image passes

## Outputs

- Candidate outputs routed to the project character reference area
- Approved portrait reference
- Approved full-body reference derived from the portrait
- Supporting angle and expression variants derived from the approved canonical ref
- Review copies mirrored into the review area

## Acceptance

- Character refs are reusable across multiple scenes and shots.
- The stage does not require a scene or shot folder unless a spec explicitly marks it clip-local.
- The approved portrait can act as the identity anchor for image-to-image full-body generation.
- The approved full-body ref can act as the source for supporting variants.


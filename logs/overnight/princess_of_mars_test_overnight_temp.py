import sys 
sys.path.insert(0, '.') 
from orchestrator.book_authoring import analyze_book 
import json 
summary = analyze_book(project_slug='princess_of_mars_test') 
print(json.dumps(summary.to_dict(), indent=2)) 

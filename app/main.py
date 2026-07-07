import json
from dataclasses import asdict

from engine.recommendation_engine import RecommendationEngine


engine = RecommendationEngine()

findings = engine.analyze()

report = [asdict(finding) for finding in findings]

print(json.dumps(report, indent=4))

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nReport saved as report.json")

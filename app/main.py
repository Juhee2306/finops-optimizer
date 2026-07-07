import os
import json
from dataclasses import asdict

from engine.recommendation_engine import RecommendationEngine


engine = RecommendationEngine()

findings = engine.analyze()
print(f"\nTotal Findings: {len(findings)}")

for finding in findings:
    print(finding.resource_type, "-", finding.issue)
report = [asdict(finding) for finding in findings]

print(json.dumps(report, indent=4))

os.makedirs("reports", exist_ok=True)

with open("reports/report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nReport saved as report.json")

from engine.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

findings = engine.analyze_ec2_instances()

for finding in findings:
    print(finding)

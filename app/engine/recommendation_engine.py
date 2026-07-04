from analyzers.ec2_analyzer import EC2Analyzer
from services.aws_client import AWSClient
from services.cloudwatch_service import CloudWatchService


class RecommendationEngine:

    def __init__(self):
        self.aws = AWSClient()
        self.cloudwatch = CloudWatchService()
        self.ec2_analyzer = EC2Analyzer()

    def analyze_ec2_instances(self):

        findings = []

        instances = self.aws.get_ec2_instances()

        for instance in instances:

            if instance["state"] == "stopped":
                print(
                    f"Instance: {instance['instance_id']} | "
                    f"State: {instance['state']}"
                )

                findings.extend(
                    self.ec2_analyzer.analyze(instance, None)
                )
                continue

            cpu = self.cloudwatch.get_average_cpu_utilization(
                instance["instance_id"]
            )

            print(
                f"Instance: {instance['instance_id']} | "
                f"State: {instance['state']} | "
                f"Type: {instance['instance_type']} | "
                f"CPU: {cpu}"
            )

            findings.extend(
                self.ec2_analyzer.analyze(instance, cpu)
            )

        return findings

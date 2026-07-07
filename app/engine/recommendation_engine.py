from analyzers.ec2_analyzer import EC2Analyzer
from analyzers.ebs_analyzer import EBSAnalyzer
from analyzers.snapshot_analyzer import SnapshotAnalyzer

from services.aws_client import AWSClient
from services.cloudwatch_service import CloudWatchService


class RecommendationEngine:

    def __init__(self):
        self.aws = AWSClient()
        self.cloudwatch = CloudWatchService()

        self.ec2_analyzer = EC2Analyzer()
        self.ebs_analyzer = EBSAnalyzer()
        self.snapshot_analyzer = SnapshotAnalyzer()

    def analyze(self):

        findings = []

        # -------------------------
        # Analyze EC2 Instances
        # -------------------------
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

        # -------------------------
        # Analyze EBS Volumes
        # -------------------------
        volumes = self.aws.get_ebs_volumes()

        for volume in volumes:
            findings.extend(
                self.ebs_analyzer.analyze(volume)
            )

        # -------------------------
        # Analyze Snapshots
        # -------------------------
        snapshots = self.aws.get_snapshots()

        for snapshot in snapshots:
            findings.extend(
                self.snapshot_analyzer.analyze(snapshot)
            )

        return findings

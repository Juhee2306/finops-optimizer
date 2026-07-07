from models.finding import Finding
from utils.pricing import EC2_MONTHLY_COST


class EC2Analyzer:

    def analyze(self, instance, cpu):

        findings = []

        # Rule 1: Stopped Instance
        if instance["state"] == "stopped":

            findings.append(
                Finding(
                    resource_id=instance["instance_id"],
                    resource_type="EC2",
                    severity="Low",
                    issue="Stopped instance",
                    recommendation="Review for termination if no longer needed",
                    estimated_monthly_savings=EC2_MONTHLY_COST.get(
                        instance["instance_type"],
                        0.0
                    )
                )
            )

            return findings

        # Rule 2: No CPU data
        if cpu is None:
            return findings

        # Rule 3: Low CPU utilization
        if cpu < 5:

            findings.append(
                Finding(
                    resource_id=instance["instance_id"],
                    resource_type="EC2",
                    severity="Medium",
                    issue="Low CPU utilization",
                    recommendation="Consider rightsizing the instance",
                    estimated_monthly_savings=EC2_MONTHLY_COST.get(
                        instance["instance_type"],
                        0.0
                    )
                )
            )

        return findings

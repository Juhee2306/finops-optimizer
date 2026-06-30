from models.finding import Finding


class EC2Analyzer:

    def analyze(self, instance, cpu):

        findings = []

        tags = instance.get("tags", [])

        environment = "unknown"

        for tag in tags:
            if tag["Key"] == "Environment":
                environment = tag["Value"].lower()

        if cpu is None:
            return findings

        if cpu < 5:

            if environment == "production":

                findings.append(
                    Finding(
                        resource_id=instance["instance_id"],
                        resource_type="EC2",
                        severity="Medium",
                        issue="Low CPU utilization",
                        recommendation="Review instance for rightsizing",
                        estimated_monthly_savings=0
                    )
                )

            else:

                findings.append(
                    Finding(
                        resource_id=instance["instance_id"],
                        resource_type="EC2",
                        severity="High",
                        issue="Low CPU utilization",
                        recommendation="Consider stopping this instance",
                        estimated_monthly_savings=0
                    )
                )

        return findings

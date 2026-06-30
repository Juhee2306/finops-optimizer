class EC2Analyzer:

    def analyze(self, instance, cpu_utilization):

        findings = []

        tags = instance.get("tags", [])

        environment = "Unknown"

        for tag in tags:
            if tag["Key"] == "Environment":
                environment = tag["Value"]

        if cpu_utilization is None:
            findings.append({
                "severity": "low",
                "issue": "No utilization data",
                "recommendation": "Review instance manually"
            })

            return findings

        if cpu_utilization < 5:

            recommendation = (
                "Review for rightsizing"
                if environment.lower() == "production"
                else "Consider stopping or rightsizing"
            )

            findings.append({
                "severity": "medium",
                "issue": "Low CPU utilization",
                "recommendation": recommendation
            })

        return findings























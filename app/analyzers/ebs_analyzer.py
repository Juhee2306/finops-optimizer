from models.finding import Finding


class EBSAnalyzer:

    def analyze(self, volume):

        findings = []

        if not volume["attached"]:

            findings.append(
                Finding(
                    resource_id=volume["volume_id"],
                    resource_type="EBS",
                    severity="High",
                    issue="Unattached volume",
                    recommendation="Delete unused volume",
                    estimated_monthly_savings=5.0
                )
            )

        return findings

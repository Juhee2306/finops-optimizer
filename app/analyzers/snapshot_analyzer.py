from datetime import datetime, timezone

from models.finding import Finding


class SnapshotAnalyzer:

    def analyze(self, snapshot):

        findings = []

        age = (
            datetime.now(timezone.utc) -
            snapshot["start_time"]
        ).days

        if age > 30:

            findings.append(
                Finding(
                    resource_id=snapshot["snapshot_id"],
                    resource_type="Snapshot",
                    severity="Medium",
                    issue=f"Snapshot is {age} days old",
                    recommendation="Review and delete if no longer required",
                    estimated_monthly_savings=2.0
                )
            )

        return findings

from dataclasses import dataclass


@dataclass
class Finding:
    resource_id: str
    resource_type: str
    severity: str
    issue: str
    recommendation: str
    estimated_monthly_savings: float

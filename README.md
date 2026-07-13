# FinOps Optimizer


```
A Python-based FinOps optimization tool that analyzes AWS resources,
identifies cost-saving opportunities, and demonstrates Infrastructure as
Code using Terraform and Docker.

```

------------------------------------------------------------------------

## Overview

FinOps Optimizer helps identify cloud resources that may be generating
unnecessary costs. It analyzes AWS resources using the AWS SDK
(`boto3`), applies optimization rules, and generates actionable
recommendations in a JSON report.

This project demonstrates practical Cloud and DevOps skills including:

-   AWS resource analysis
-   FinOps principles
-   Infrastructure as Code (Terraform)
-   Containerization (Docker)
-   Python automation

------------------------------------------------------------------------

# Problem Statement

Cloud resources are often left running or over-provisioned, increasing
operational costs.

This project automates the discovery of selected AWS resources and
generates recommendations to help improve cloud cost efficiency.

------------------------------------------------------------------------

# Features

-   Analyze EC2 instances
-   Detect stopped EC2 instances
-   Detect low CPU utilization
-   Analyze EBS volumes
-   Analyze snapshots
-   Estimate monthly savings
-   Generate JSON optimization reports
-   Dockerized application
-   Terraform-based AWS infrastructure provisioning

------------------------------------------------------------------------

# Tech Stack

  Category           Technology
  ------------------ --------------
  Language           Python 3
  Cloud              AWS
  SDK                boto3
  Infrastructure     Terraform
  Containerization   Docker
  Version Control    Git & GitHub

------------------------------------------------------------------------

# Project Structure

``` text
finops-optimizer/
│
├── app/
│   ├── analyzers/
│   ├── engine/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── terraform/
├── reports/
├── assets/
├── Dockerfile
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# Architecture

> Replace this section with the architecture diagram image later.

``` text
Terraform
      │
      ▼
AWS Infrastructure
      │
      ▼
AWS SDK (boto3)
      │
      ▼
Recommendation Engine
      │
      ├── EC2 Analyzer
      ├── EBS Analyzer
      └── Snapshot Analyzer
      │
      ▼
JSON Report
```

------------------------------------------------------------------------

# How It Works

1.  Connects to AWS using configured credentials.
2.  Discovers supported AWS resources.
3.  Retrieves CPU utilization using CloudWatch (where applicable).
4.  Applies optimization rules.
5.  Estimates potential monthly savings.
6.  Generates a structured JSON report.

------------------------------------------------------------------------

# Running Locally

``` bash
git clone https://github.com/YOUR_USERNAME/finops-optimizer.git
cd finops-optimizer

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app/main.py
```

------------------------------------------------------------------------

# Docker

Build:

``` bash
docker build -t finops-optimizer .
```

Run:

``` bash
docker run --rm \
-v ~/.aws:/root/.aws:ro \
finops-optimizer
```

------------------------------------------------------------------------

# Terraform

``` bash
cd terraform

terraform init
terraform validate
terraform plan
terraform apply
```

Destroy infrastructure:

``` bash
terraform destroy
```

------------------------------------------------------------------------

# Sample Output

``` json
[
  {
    "resource_type": "EC2",
    "issue": "Stopped instance",
    "recommendation": "Review for termination if no longer needed",
    "estimated_monthly_savings": 7.5
  }
]
```

------------------------------------------------------------------------

# Screenshots

> Replace the placeholders below after renaming your screenshots.

-   Project Execution
-   Docker Build & Run
-   Terraform Plan
-   Terraform Apply
-   AWS EC2 Console
-   JSON Report
-   Project Structure
-   VPC
-   Security Group
-   Terraform Destroy

------------------------------------------------------------------------

# Skills Demonstrated

-   AWS EC2
-   CloudWatch
-   FinOps Fundamentals
-   Infrastructure as Code
-   Docker
-   Python Automation
-   Git & GitHub
-   Cost Optimization
-   Cloud Resource Analysis

------------------------------------------------------------------------

# Future Enhancements

-   Support additional AWS services
-   Export reports in CSV and HTML
-   Web dashboard
-   Scheduled scans
-   Cost Explorer integration
-   Email notifications

------------------------------------------------------------------------

# Author

**Juhee Lavanya**

Cloud Computing Undergraduate \| Aspiring Cloud & DevOps Engineer

LinkedIn: 

GitHub: 



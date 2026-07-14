# FinOps Optimizer


A Cloud Cost Optimization platform built with Python, AWS, Docker, and Terraform that automatically analyzes AWS resources and generates actionable FinOps 
recommendations.

------------------------------------------------------------------------

## Overview

Cloud environments often contain idle or underutilized resources that unnecessarily increase operational costs. Manually identifying these inefficiencies is time-consuming and prone to oversight.

**FinOps Optimizer** automates this process by discovering AWS resources, analyzing their utilization using the AWS SDK (`boto3`), applying FinOps optimization rules, estimating potential monthly savings, and generating actionable recommendations in a structured JSON report.

This project demonstrates practical Cloud and DevOps skills through the implementation of Infrastructure as Code (Terraform), containerization (Docker), AWS automation, and Python-based cloud resource analysis.

 **Developed as a portfolio project to demonstrate Cloud Computing, DevOps, and FinOps practices using AWS.**

------------------------------------------------------------------------

# Problem Statement

Cloud environments often contain idle, underutilized, or forgotten resources that continue to incur unnecessary costs. Identifying these resources manually becomes increasingly difficult as cloud infrastructure grows, making cost optimization a continuous challenge for organizations.

The objective of this project is to automate the discovery and analysis of AWS resources, identify potential cost-saving opportunities, and provide actionable recommendations using FinOps best practices.

By combining AWS APIs, Python automation, Docker, and Terraform, this project demonstrates how cloud infrastructure can be analyzed and managed efficiently while promoting Infrastructure as Code (IaC) and modern DevOps practices.

------------------------------------------------------------------------
# 🎯 Project Objectives

- Automate the discovery of AWS cloud resources.
- Analyze EC2 instances, EBS volumes, and snapshots for optimization opportunities.
- Detect stopped and underutilized EC2 instances using CloudWatch metrics.
- Estimate potential monthly cost savings for identified resources.
- Generate structured JSON reports with optimization recommendations.
- Demonstrate Infrastructure as Code (IaC) using Terraform.
- Containerize the application using Docker for portability and reproducibility.
- Showcase practical Cloud Computing, FinOps, and DevOps skills through an end-to-end project.

---------------------------------------------------------------------------


# Features

| Feature | Description |
|----------|-------------|
| **AWS Resource Discovery** | Automatically discovers EC2 instances, EBS volumes, and EBS snapshots within the configured AWS region. |
| **EC2 Analysis** | Identifies stopped EC2 instances and detects underutilized instances using CloudWatch CPU utilization metrics. |
| **EBS Volume Analysis** | Detects unattached EBS volumes that may be generating unnecessary storage costs. |
| **Snapshot Analysis** | Identifies snapshots that can be reviewed for cleanup and storage optimization. |
| **Cost Estimation** | Estimates potential monthly savings for identified optimization opportunities. |
| **Recommendation Engine** | Applies FinOps rules to generate actionable optimization recommendations. |
| **JSON Report Generation** | Generates structured JSON reports containing findings and recommendations. |
| **Docker Support** | Containerized application for consistent deployment across environments. |
| **Infrastructure as Code** | Uses Terraform to provision AWS infrastructure including VPC, networking, security groups, and EC2 instances. |
| **AWS SDK Integration** | Uses the AWS SDK (`boto3`) for secure interaction with AWS services. |

------------------------------------------------------------------------

---

# Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python 3 |
| **Cloud Platform** | Amazon Web Services (AWS) |
| **Cloud SDK** | boto3 |
| **Infrastructure as Code** | Terraform |
| **Containerization** | Docker |
| **Version Control** | Git & GitHub |
| **Monitoring** | Amazon CloudWatch |
| **Operating System** | Ubuntu (WSL) |

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



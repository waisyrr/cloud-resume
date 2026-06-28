# 🚀 AWS Cloud Resume Challenge

> **Production-grade serverless cloud portfolio built on AWS using Terraform, GitHub Actions, and modern cloud engineering best practices.**

[🌐 Live Website](https://d1l6jcvu4zf64q.cloudfront.net/) • [🔌 Visitor Counter API](https://t9bxl7c440.execute-api.eu-north-1.amazonaws.com/counter)

---

# ⚡ Understand This Project in 10 Seconds

This project demonstrates the complete lifecycle of a modern AWS serverless application.

✅ Infrastructure provisioned with **Terraform**

✅ Static website hosted on **Amazon S3**

✅ Global delivery through **CloudFront**

✅ Serverless backend using **AWS Lambda**

✅ REST API with **API Gateway**

✅ Persistent visitor counter stored in **DynamoDB**

✅ Automated deployments using **GitHub Actions**

✅ Secure cloud architecture with **IAM**

---

# 🏗️ Architecture

![Architecture Diagram](architecture6.png)

**Request Flow**

```text
1️⃣ Browser requests website
        │
        ▼
CloudFront (CDN)
        │
        ▼
Amazon S3 (Portfolio)

────────────────────────────

2️⃣ Visitor count request (via JavaScript)
        │
        ▼
API Gateway
        │
        ▼
AWS Lambda (Python)
        │
        ▼
Amazon DynamoDB
        │
        ▼
Visitor count returned to browser
```

---

# ✨ Key Features

- ☁️ Serverless AWS architecture
- 🏗️ Infrastructure as Code (Terraform)
- 🚀 Automated CI/CD with GitHub Actions
- 🌍 Global content delivery using CloudFront
- 💾 Persistent visitor counter with DynamoDB
- ⚡ AWS Lambda backend (Python)
- 🔌 REST API using API Gateway
- 🔒 HTTPS-secured application
- 📈 Atomic visitor count updates
- 🔄 Automatic CloudFront cache invalidation
- 📦 Fully reproducible infrastructure

---

# 🛠️ AWS Services Used

| Service | Purpose |
|----------|---------|
| ☁️ Amazon S3 | Static website hosting |
| 🌍 Amazon CloudFront | Global CDN |
| ⚡ AWS Lambda | Serverless backend |
| 🔌 API Gateway | REST API |
| 💾 DynamoDB | Visitor counter database |
| 🔐 IAM | Identity & permissions |
| 🏗️ Terraform | Infrastructure as Code |
| 🚀 GitHub Actions | CI/CD deployment pipeline |

---

# 📂 Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD Pipeline
│
├── backend/
│   └── lambda_function.py      # Visitor Counter API
│
├── terraform/
│   ├── main.tf                 # AWS Infrastructure
│   ├── variables.tf
│   └── outputs.tf
│
├── index.html                  # Portfolio Website
│
└── README.md
```

---

# 🚀 Deployment Workflow

```text
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Upload Website to Amazon S3
    │
    ▼
CloudFront Cache Invalidation
    │
    ▼
Website Updated Globally
```

---

# 🔌 API

### Endpoint

```http
POST /counter
```

### Response

```json
{
  "count": 95
}
```

---

# 💡 Engineering Highlights

### 🏗️ Infrastructure as Code

Every AWS resource is provisioned using Terraform, allowing repeatable, version-controlled infrastructure deployments.

---

### ⚡ Serverless Architecture

No virtual machines or servers are managed. AWS automatically scales the application based on demand.

---

### 🚀 CI/CD Automation

Every push to the `main` branch automatically:

- Uploads the website to Amazon S3
- Invalidates the CloudFront cache
- Deploys the latest version globally

---

### 💾 Atomic Visitor Counter

The visitor counter is powered by DynamoDB atomic update operations, ensuring accurate counts during concurrent requests.

---

### 🌍 Global Performance

CloudFront distributes website content through AWS edge locations, reducing latency worldwide.

---

# 🛡️ Security

- 🔐 HTTPS via CloudFront
- 🔑 IAM Roles for AWS services
- 🌐 API Gateway CORS configuration
- 🚫 No servers to patch or maintain
- ☁️ Fully managed AWS services

---

# 📚 Skills Demonstrated

### Cloud

- AWS Architecture
- Serverless Computing
- Cloud Infrastructure
- Cloud Security

### DevOps

- Infrastructure as Code (Terraform)
- CI/CD Pipelines
- GitHub Actions
- Automated Deployments

### Backend

- AWS Lambda
- REST APIs
- API Gateway
- Python

### Data

- DynamoDB
- NoSQL Databases
- Atomic Database Operations

### Infrastructure

- Amazon S3
- Amazon CloudFront
- IAM
- HTTPS
- CDN Architecture

---

# 🎯 Project Goal

The Cloud Resume Challenge bridges the gap between cloud certifications and real-world engineering by demonstrating the ability to design, provision, automate, deploy, secure, and operate a complete production-style serverless application on AWS.

---

## ⭐ Technologies

**AWS • Terraform • GitHub Actions • Amazon S3 • CloudFront • API Gateway • AWS Lambda • DynamoDB • IAM • Python • HTML • CSS • JavaScript • CI/CD • Infrastructure as Code • Serverless Computing**
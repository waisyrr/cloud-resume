# Serverless Cloud Resume Challenge

Static resume website with a live visitor counter built using AWS serverless services.

## Live Demo
- Website: https://your-cloudfront-url
- API: https://your-api-id.execute-api.region.amazonaws.com/getcount

---

## What it does

- Displays a static resume hosted on Amazon S3
- Serves content globally via Amazon CloudFront (HTTPS enabled)
- Tracks page visits using a DynamoDB table
- Uses AWS Lambda (Python + boto3) to increment and return visitor count
- Frontend fetches live counter from API Gateway endpoint
- Automatically deploys updates via GitHub Actions CI/CD

---

## Architecture

S3 (frontend) → CloudFront → API Gateway → Lambda → DynamoDB

---

## Tech Stack

- Amazon S3
- Amazon CloudFront
- AWS Lambda (Python)
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- GitHub Actions

---

## API

### GET /getcount

Returns current visitor count.

Example response:

{
  "count": 42
}

---

## Setup (optional)

1. Create and configure S3 bucket for static hosting
2. Upload `index.html`
3. Create DynamoDB table: `cloud-resume-counter`
4. Deploy Lambda function with DynamoDB permissions
5. Create API Gateway route `/getcount`
6. Connect frontend fetch request to API endpoint
7. Set up GitHub Actions for automated deployment

---

## Notes

- Ensure CORS is enabled on API Gateway
- CloudFront is used for HTTPS + caching
- IAM roles follow least-privilege access

---

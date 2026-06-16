# 🚀 Serverless Cloud Resume Challenge



Static resume website with a live visitor counter built using AWS serverless services.



## 🌐 Live Demo



- 💻 **Live Website:** https://d1l6jcvu4zf64q.cloudfront.net/

- ⚙️ **Live Visitor Counter API:** https://25ktpno81j.execute-api.eu-north-1.amazonaws.com/getcount



---



## 📋 What it does



- 📄 Serves a static resume website hosted on Amazon S3  

- ⚡ Delivers content globally via Amazon CloudFront (HTTPS enabled)  

- 📊 Tracks page visits using Amazon DynamoDB  

- 🧠 Uses AWS Lambda (Python + boto3) to increment and return visitor count  

- 🔌 Frontend fetches live visitor count via API Gateway endpoint  

- 🤖 Automated deployments using GitHub Actions CI/CD pipeline  



---



## 🏗️ Architecture



Frontend (S3 + CloudFront) → API Gateway → Lambda (Python) → DynamoDB



![Project Architecture Diagram](architecture.png)



---



## 🛠️ Tech Stack



- 🪣 Amazon S3  

- 🌐 Amazon CloudFront  

- ⚡ AWS Lambda (Python)  

- ⚙️ Amazon API Gateway (HTTP API)  

- 💾 Amazon DynamoDB  

- 🤖 GitHub Actions  



---



## 🔌 API



### GET /getcount



Returns the current visitor count stored in DynamoDB.



#### Response



```json

{

  "count": 42

}

````



---



## 🚀 Deployment Steps



1. 🪣 Create and configure S3 bucket for static website hosting

2. 📄 Upload `index.html` and frontend assets

3. 💾 Create DynamoDB table: `cloud-resume-counter`

4. ⚡ Deploy Lambda function with DynamoDB permissions

5. ⚙️ Create API Gateway route `/getcount` connected to Lambda

6. 🔌 Update frontend to call API Gateway endpoint

7. 🤖 Configure GitHub Actions for automated deployment



---



## 💡 Notes



* 🔑 Ensure CORS is enabled on API Gateway

* 💨 CloudFront provides HTTPS and caching

* 🔒 IAM roles follow least-privilege access principles



```

```
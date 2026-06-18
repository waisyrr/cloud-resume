variable "aws_region" {
  type        = string
  default     = "eu-north-1"
  description = "The target AWS region for deployment"
}

variable "bucket_name" {
  type        = string
  default     = "wais-cloud-resume-2026"
  description = "The globally unique name for the static website S3 bucket"
}

variable "dynamodb_table_name" {
  type        = string
  default     = "cloud-resume-counter"
  description = "The name of the visitor counter DynamoDB table"
}
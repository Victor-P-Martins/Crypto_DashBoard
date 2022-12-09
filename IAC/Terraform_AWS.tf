terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["/Users/victo/.aws/credentials"]
}

#Bucket S3 Crypto Dash 

resource "aws_s3_bucket" "crypto_dash" {
  bucket = "crypto-dash-bucket-app"

  tags = {
    Name        = "Bucket Crypto Dashboard Streamlit"
    Environment = "Dev"
  }
}

# ACL Configuration Bucket S3

resource "aws_s3_bucket_acl" "crypto_dash" {
  bucket = aws_s3_bucket.crypto_dash.id
  acl    = "private"
}

#Configure Versioning Disabled


resource "aws_s3_bucket_versioning" "crypto_dash" {
  bucket = aws_s3_bucket.crypto_dash.id
  versioning_configuration {
    status = "Disabled"
  }
}


# IAM Policy S3

resource "aws_iam_policy" "policy" {
  name        = "policy_aws"
  path        = "/"
  description = "My policy s3 bucket"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "ConsoleAccess"
        Effect = "Allow"
        Action = ["s3:*"]
        Resource = [
          "arn:aws:s3:::crypto-dash-bucket-app",
          "arn:aws:s3:::crypto-dash-bucket-app/*"
        ]
      },
    ]
  })
}

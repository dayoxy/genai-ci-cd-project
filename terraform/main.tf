provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "genai_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with the appropriate AMI
  instance_type = var.instance_type

  tags = {
    Name = "GenAI-Instance"
  }
}

resource "aws_s3_bucket" "genai_bucket" {
  bucket = "genai-data-bucket"
  acl    = "private"
}

output "instance_public_ip" {
  value = aws_instance.genai_instance.public_ip
}

output "s3_bucket_name" {
  value = aws_s3_bucket.genai_bucket.bucket
}

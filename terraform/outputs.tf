output "instance_public_ip" {
  value = aws_instance.genai_instance.public_ip
}

output "s3_bucket_name" {
  value = aws_s3_bucket.genai_bucket.bucket
}

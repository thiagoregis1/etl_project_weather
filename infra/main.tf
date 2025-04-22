provider "aws" {
  region = "us-east-1" # Substitua pela região desejada
}

resource "aws_s3_bucket" "etl_bucket" {
  bucket = "etl-project-weather-bucket" # Substitua pelo nome do bucket desejado
  acl    = "private"

  tags = {
    Name        = "ETL Project Weather Bucket"
    Environment = "Production"
  }
}

resource "aws_s3_bucket_policy" "etl_bucket_policy" {
  bucket = aws_s3_bucket.etl_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowPublicRead"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.etl_bucket.arn}/*"
      }
    ]
  })
}

#CRIAR RDS PARA ARMAZENAR OS DADOS DO ETL, PARA CONECTAR VIA SCRIPT PRECISA LIBERAR A PORTA TCP O BANCO DE DADOS
import boto3
import os


def download_from_s3(bucket: str, key: str, dest_path: str) -> str:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "us-east-1"),
    )
    s3.download_file(bucket, key, dest_path)
    return dest_path

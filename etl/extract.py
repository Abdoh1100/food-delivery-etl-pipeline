import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def download_from_s3(bucket: str, s3_key: str, dest_path: str) -> str:
    """
    Downloads a file from S3 to a local path.
    Returns the local path on success.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    print(f"Downloading s3://{bucket}/{s3_key} → {dest_path}")
    s3.download_file(bucket, s3_key, dest_path)
    print("Download complete.")
    return dest_path

import os
from dotenv import load_dotenv
from etl.extract import download_from_s3
from etl.transform import clean_orders
from etl.load import insert_orders

load_dotenv()

RAW_PATH = "data/raw/orders.csv"


def run():
    print("Extract: downloading from S3...")
    download_from_s3(
        bucket=os.getenv("S3_BUCKET"),
        s3_key=os.getenv("S3_KEY"),
        dest_path=RAW_PATH,
    )

    print("Transform: cleaning data...")
    df = clean_orders(RAW_PATH)

    print(f"Load: inserting {len(df)} rows into PostgreSQL...")
    insert_orders(df)

    print("Pipeline complete.")


if __name__ == "__main__":
    run()

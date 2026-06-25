import os
import psycopg2
import pandas as pd
from psycopg2.extras import execute_values


def get_connection():
    return psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT", 5432),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
    )


def insert_orders(df: pd.DataFrame) -> None:
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            rows = [tuple(row) for row in df.itertuples(index=False)]
            cols = ", ".join(df.columns)
            execute_values(
                cur,
                f"INSERT INTO orders ({cols}) VALUES %s ON CONFLICT (order_id) DO NOTHING",
                rows,
            )
        conn.commit()
    finally:
        conn.close()

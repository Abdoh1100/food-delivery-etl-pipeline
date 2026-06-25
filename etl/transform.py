import pandas as pd


def clean_orders(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["order_id"], inplace=True)
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    return df

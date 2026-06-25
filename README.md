# Food Delivery ETL Pipeline

Extracts order CSVs from S3, cleans them with pandas, and loads them into PostgreSQL.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your credentials
```

## Database

```bash
psql -U postgres -d food_delivery -f sql/schema.sql
```

## Run

```bash
python pipeline.py
```

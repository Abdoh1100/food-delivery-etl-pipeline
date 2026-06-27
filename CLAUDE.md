# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (activate venv first)
source venv/bin/activate
pip install -r requirements.txt

# Apply database schema
psql -U postgres -d food_delivery -f sql/schema.sql

# Run the full pipeline
python pipeline.py

# Run tests
python -m pytest tests/
```

## Architecture

The pipeline runs in three sequential stages, each in its own module under `etl/`:

1. **extract.py** — downloads a single CSV from S3 using `boto3` and writes it to `data/raw/orders.csv`.
2. **transform.py** — reads that CSV with `pandas`, normalises column names, deduplicates, drops rows missing `order_id`, and coerces `created_at` to datetime.
3. **load.py** — bulk-inserts the cleaned DataFrame into PostgreSQL via `psycopg2.extras.execute_values`, skipping rows that already exist (`ON CONFLICT (order_id) DO NOTHING`).

`pipeline.py` is the entry point that calls these three functions in order. All credentials are read from environment variables (loaded from `.env` via `python-dotenv`).

## Environment Variables

Copy `.env.example` to `.env` and fill in values before running. Required vars:

| Group | Variables |
|-------|-----------|
| AWS | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET`, `S3_KEY` |
| PostgreSQL | `PG_HOST`, `PG_PORT`, `PG_DB`, `PG_USER`, `PG_PASSWORD` |

## Database

The target table is `orders` in the `food_delivery` database (see `sql/schema.sql`). The load step dynamically builds the `INSERT` column list from the DataFrame columns, so the DataFrame column names must match the table columns exactly after `transform.py` normalises them.

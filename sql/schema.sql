CREATE TABLE IF NOT EXISTS orders (
    order_id      VARCHAR(64)   PRIMARY KEY,
    customer_id   VARCHAR(64),
    restaurant_id VARCHAR(64),
    status        VARCHAR(32),
    total_amount  NUMERIC(10, 2),
    created_at    TIMESTAMP
);

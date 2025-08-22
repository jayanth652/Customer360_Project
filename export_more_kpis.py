import sqlite3
import pandas as pd
import os

# Connect to the database
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "customer360.db")
EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "exports")

os.makedirs(EXPORT_DIR, exist_ok=True)
conn = sqlite3.connect(DB_PATH)

# --- Top Products by Revenue ---
top_products = pd.read_sql_query("""
    SELECT product_id, SUM(line_total) as revenue
    FROM v_order_details
    GROUP BY product_id
    ORDER BY revenue DESC
    LIMIT 10;
""", conn)
top_products.to_csv(os.path.join(EXPORT_DIR, "top_products.csv"), index=False)

# --- Customer Retention ---
retention = pd.read_sql_query("""
    SELECT 
        CASE WHEN order_count=1 THEN 'One-time Buyer' ELSE 'Repeat Buyer' END AS customer_type,
        COUNT(*) as num_customers
    FROM (
        SELECT customer_id, COUNT(order_id) as order_count
        FROM v_order_details
        GROUP BY customer_id
    )
    GROUP BY customer_type;
""", conn)
retention.to_csv(os.path.join(EXPORT_DIR, "customer_retention.csv"), index=False)

# --- Average Order Value by Region ---
aov = pd.read_sql_query("""
    SELECT region, AVG(line_total) as avg_order_value
    FROM v_order_details
    GROUP BY region;
""", conn)
aov.to_csv(os.path.join(EXPORT_DIR, "avg_order_value.csv"), index=False)

print("✅ Extra exports created in 'exports/' folder")
conn.close()

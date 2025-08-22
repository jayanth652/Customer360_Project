
import sqlite3, pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DB = BASE/"customer360.db"

def main():
    conn = sqlite3.connect(DB)
    for name in ["customers","products","orders","order_items"]:
        df = pd.read_csv(BASE/"data"/f"{name}.csv")
        df.to_sql(name, conn, if_exists="replace", index=False)
    conn.execute("""
        CREATE VIEW IF NOT EXISTS v_order_details AS
        SELECT oi.order_id,o.customer_id,o.order_date,c.country,c.region,oi.product_id,oi.unit_price,oi.quantity,(oi.unit_price*oi.quantity) AS line_total
        FROM order_items oi
        JOIN orders o ON oi.order_id=o.order_id
        JOIN customers c ON o.customer_id=c.customer_id;
    """)
    conn.commit()
    conn.close()
    print("✅ Loaded data into customer360.db")

if __name__=="__main__":
    main()

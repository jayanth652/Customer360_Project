
import sqlite3, pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DB = BASE/"customer360.db"
OUT = BASE/"exports"
OUT.mkdir(exist_ok=True)

def q(sql):
    with sqlite3.connect(DB) as conn:
        return pd.read_sql_query(sql, conn)

def main():
    q1 = q("SELECT region,SUM(line_total) as revenue FROM v_order_details GROUP BY region;")
    q1.to_csv(OUT/"sales_by_region.csv", index=False)

    q2 = q("SELECT substr(order_date,1,7) as ym,SUM(line_total) as revenue FROM v_order_details GROUP BY ym;")
    q2.to_csv(OUT/"monthly_revenue.csv", index=False)

    print("✅ Exported CSVs for Tableau")

if __name__=="__main__":
    main()

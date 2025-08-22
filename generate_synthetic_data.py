
import os, random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from faker import Faker

NUM_CUSTOMERS = 1000
NUM_PRODUCTS  = 200
NUM_ORDERS    = 2000

BASE_DIR = os.path.dirname(__file__)
rng = np.random.default_rng(42)
fake = Faker()

def make_customers(n=NUM_CUSTOMERS):
    rows = []
    for i in range(n):
        cid = f"C{str(i).zfill(5)}"
        rows.append({
            "customer_id": cid,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "region": fake.state()
        })
    return pd.DataFrame(rows)

def make_products(n=NUM_PRODUCTS):
    cats = ["Office","Tech","Furniture"]
    rows = []
    for i in range(n):
        pid = f"P{str(i).zfill(4)}"
        price = float(np.round(rng.uniform(5,500),2))
        rows.append({"product_id": pid,"category": random.choice(cats),"name": f"Product {pid}","price": price})
    return pd.DataFrame(rows)

def make_orders(n=NUM_ORDERS, customers=None):
    start = datetime.now()-timedelta(days=365)
    rows = []
    for i in range(n):
        oid = f"O{str(i).zfill(6)}"
        cid = customers.sample(1)["customer_id"].iloc[0]
        od = start+timedelta(days=int(rng.integers(0,365)))
        rows.append({"order_id": oid,"customer_id": cid,"order_date": od.date().isoformat()})
    return pd.DataFrame(rows)

def make_order_items(orders, products):
    rows = []
    for _,o in orders.iterrows():
        k = int(rng.integers(1,4))
        for _ in range(k):
            p = products.sample(1).iloc[0]
            qty = int(rng.integers(1,5))
            rows.append({"order_id":o["order_id"],"product_id":p["product_id"],"unit_price":p["price"],"quantity":qty})
    return pd.DataFrame(rows)

def main():
    customers = make_customers()
    products  = make_products()
    orders    = make_orders(customers=customers)
    order_items = make_order_items(orders, products)

    customers.to_csv(os.path.join(BASE_DIR,"customers.csv"),index=False)
    products.to_csv(os.path.join(BASE_DIR,"products.csv"),index=False)
    orders.to_csv(os.path.join(BASE_DIR,"orders.csv"),index=False)
    order_items.to_csv(os.path.join(BASE_DIR,"order_items.csv"),index=False)
    print("✅ Synthetic CSVs written")

if __name__ == "__main__":
    main()

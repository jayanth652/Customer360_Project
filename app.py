
from flask import Flask,request,jsonify
import joblib, sqlite3, pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
MODEL = BASE/"ml"/"churn_model.pkl"
DB = BASE/"customer360.db"

app = Flask(__name__)
clf = joblib.load(MODEL)

@app.route("/churn_score")
def churn_score():
    cid = request.args.get("customer_id")
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql_query(f"SELECT COUNT(order_id) as n_orders,SUM(line_total) as spend FROM v_order_details WHERE customer_id='{cid}'", conn)
    if df.empty: return jsonify({"error":"customer not found"})
    proba = clf.predict_proba(df)[0,1]
    return jsonify({"customer_id":cid,"churn_probability":float(proba)})

if __name__=="__main__":
    app.run(debug=True)

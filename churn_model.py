
import sqlite3, joblib, pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

BASE = Path(__file__).resolve().parents[1]
DB = BASE/"customer360.db"
MODEL = BASE/"ml"/"churn_model.pkl"

def load_data():
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql_query("SELECT customer_id,COUNT(order_id) as n_orders, SUM(line_total) as spend FROM v_order_details GROUP BY customer_id;", conn)
    df["churn"] = (df["n_orders"]==1).astype(int)
    return df

def main():
    df = load_data()
    X = df[["n_orders","spend"]]
    y = df["churn"]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test,y_pred))
    joblib.dump(clf, MODEL)
    print(f"✅ Model saved at {MODEL}")

if __name__=="__main__":
    main()

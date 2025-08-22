# Customer360 – End-to-End Data Analytics & ML Pipeline

🔗 [View Interactive Tableau Dashboard](https://public.tableau.com/views/https://public.tableau.com/app/profile/jayanth.alluri/viz/Customer360AnalyticsDashboard/Dashboard1?publish=yes)

## 📌 Project Overview
Customer360 simulates an e-commerce business to demonstrate a **full data pipeline**:
- Data generation with Python (synthetic customer, order, and product data)
- ETL pipeline → SQLite database
- KPI calculation: revenue, churn %, customer retention
- Tableau dashboards for **sales, revenue trends, top products, customer insights**
- ML churn prediction model (Random Forest, deployed with Flask API)

## 🛠️ Tech Stack
- **Python** (pandas, scikit-learn, Flask, Faker)
- **SQL (SQLite)**
- **Tableau Public**
- **GitHub** for project portfolio

## 📊 Dashboards
- Sales by Region (Bar Chart)
- Monthly Revenue Trend (Line Chart)
- Top 10 Products by Revenue (Bar Chart)
- Customer Retention (Pie Chart)
- Avg Order Value by Region (Bar Chart)
- KPI Summary (Total Revenue, Customers, Repeat %)

👉 [View Dashboard](https://public.tableau.com/app/profile/jayanth.alluri/viz/Customer360AnalyticsDashboard/Dashboard1?publish=yes)

## 🚀 How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/YourUsername/Customer360_Project.git
   cd Customer360_Project
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run ETL pipeline
   ```bash
   python etl/etl_pipeline.py
4. Export analytics for Tableau
   ```bash
   python analysis/export_for_tableau.py
   python analysis/export_more_kpis.py
5. Start Flask API
   ```bash
   python app/app.py
6. API Example
   ```json
   { "customer_id": "C00001", "churn_probability": 0.12 }



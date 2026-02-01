# 🚕 Uber Trip Analysis using Machine Learning

This project analyzes Uber trip demand using historical trip data (Jan–Feb).
It focuses on identifying demand patterns, understanding the relationship between trips and active vehicles, and building a machine learning model to predict future trip demand.

In addition to ML analysis, the project also includes:

- A Python Dashboard (Streamlit App)
- A Power BI Dashboard 

This makes the project a complete end-to-end data analytics.

---

## 📌 What This Project Includes
### 🔹 Data Analysis

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Demand trend visualizations
- Relationship analysis between trips and active vehicles

### 🔹 Machine Learning

- Model to predict daily trip demand
- Model evaluation and performance analysis
- Actual vs Predicted comparison

### 🔹 Dashboards

- Python Dashboard (Streamlit) 
- Power BI Dashboard 

---

## 📂 Dataset

The dataset contains daily aggregated Uber trip records with fields such as:

- date
- trips
- active_vehicles
- dispatching_base_number

---

## 🛠 Tools Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (Machine Learning)
- Streamlit (Python Dashboard)

---

## 📊 Main Analysis & Visualizations

## 🔍 Exploratory Data Analysis (EDA)

- Daily Trips Trend
- Active Vehicles Trend
- Trips vs Active Vehicles (relationship)
- Weekday-wise Demand Analysis
- Correlation Heatmap
- 7-Day Moving Average Trend

## 🤖 Machine Learning

- Actual vs Predicted Trips
- Model Error Distribution

**All generated charts are saved inside the images/ folder.**

---

## 🧠 Key Insights

1. Uber trip demand varies significantly across days, with clear peak periods.
2. Active vehicles increase during high-demand days, showing supply adjustment.
3. Trips and active vehicles show a strong positive relationship.
4. Weekday analysis helps identify high-demand days for planning.
5. The ML model captures demand patterns and predicts trips with reasonable accuracy.

---

## 🖥 Python Interactive Dashboard (Streamlit)

An analytical dashboard built using Streamlit + Plotly to explore trip demand patterns interactively.

Features:

- KPI cards (Trips, Vehicles, Peak Day, etc.)
- Trip demand trend with moving average
- Vehicles vs Trips correlation
- Trips by weekday & month
- Base-wise performance analysis
- 7-Day trip forecast

**📁 File: app/app.py**

---

## 📊 Power BI Dashboard

A professional Power BI dashboard with interactive navigation tabs:
Pages Included:

- Overview
(KPIs, Trip Trend, Weekday Pattern, Month Distribution, Top Bases)
- Base Analysis
(Base contribution, Heatmap, Trips by Base Trend)
- Prediction
(Trips forecast, Breakdown analysis, Key influencers)

**📁 File:PowerBi_Dashboard/Uber_Trip_Analysis_Dashboard.pbix**

---

## 📁 Folder Structure

Uber-Trip-Analysis-ML/
│
├── PowerBi_Dashboard/
│   └── Uber_Trip_Analysis_Dashboard.pbix
│
├── app/
│   └── app.py                
│
├── data/
│   └── Uber-Jan-Feb-FOIL.csv 
│
├── images/
│   ├── eda/
│   └── ml/
│
├── notebook/
│   └── Uber_Trip_Analysis_ML.ipynb
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run This Project
### 🔹 1. Clone the Repository
git clone https://github.com/aparna190417/Uber-Trip-Analysis-ML.git
cd Uber-Trip-Analysis-ML

### 🔹 2. Install Requirements
pip install -r requirements.txt

### 🔹 3. Run Jupyter Notebook (ML + EDA)
jupyter notebook
Open:
notebook/Uber_Trip_Analysis_ML.ipynb

### 🔹 4. Run Python Dashboard (Streamlit)
cd app
streamlit run app.py
Dashboard will open in your browser 🚀

### 🔹 5. Open Power BI Dashboard

Open this file in Power BI Desktop:
PowerBi_Dashboard/Uber_Trip_Analysis_Dashboard.pbix

---

## 👩‍💻 Author

**Aparna Patel**

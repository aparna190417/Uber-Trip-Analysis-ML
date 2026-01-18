# Uber Trip Analysis using Machine Learning

This project analyzes Uber trip demand using historical trip data (Jan–Feb).  
It focuses on identifying demand patterns over time, the relationship between trips and active vehicles, and finally builds a machine learning model to predict trip demand.

---

## What this project includes

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Demand trend visualizations
- Relationship analysis between trips and active vehicles
- Machine Learning model for trip demand prediction
- Model evaluation and performance plots

---

## Dataset

The dataset contains daily records with fields like:
- `date`
- `trips`
- `active_vehicles`

---

## Tools used

- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (for ML)

---

## Main analysis / graphs

### EDA
- Daily Trips Trend
- Active Vehicles Trend
- Trips vs Active Vehicles (relationship)
- Weekday-wise Demand Analysis
- Correlation Heatmap
- Moving Average Trend (7-day)

### ML
- Actual vs Predicted Trips (model performance)
- Error distribution / residual analysis

(All output charts are saved in the `images/` folder.)

---

## Key insights

- Uber trip demand changes significantly across days, with clear peak periods.
- Active vehicles generally increase during higher demand days, showing supply adjustment.
- Trips and active vehicles have a positive relationship (higher vehicles → higher fulfilled demand).
- Weekday analysis helps identify high-demand days for better planning.
- The ML model is able to capture demand patterns and predict trips with reasonable accuracy.

---

## Folder structure

Uber-Trip-Analysis-ML/
|── powerbi_dashboard/
│── notebook/
│── data/
│── images/
│ ├── eda/
│ └── ml/
│── requirements.txt
│── README.md
│── .gitignore

---

## Sample Visualizations

![Daily Trips Trend](images/eda/01_daily_trips_trend.png)

![Active Vehicles Trend](images/eda/02_active_vehicles_trend.png)

![Trips vs Active Vehicles](images/eda/03_trips_vs_active_vehicles.png)

![Weekday wise demand](images/eda/04_weekday_demand.png)

![Correlation Heatmap](images/eda/05_correlation_heatmap.png)

![Moving Average Trend](images/eda/06_trips_moving_avg.png)

![Actual vs Predicted](images/ml/01_actual_vs_predicted_sorted_date.png)

![Error Distribution](images/ml/02_error_distribution.png)

---

## Power BI Dashboard 

A professional **Power BI dashboard** has been created with interactive navigation tabs:

✅ **Overview** (KPIs + Trend + Weekday + Month distribution + Top bases)  
✅ **Base Analysis** (Top bases + Heatmap + Base contribution + Trend by base)  
✅ **Prediction** (Trips forecast + Breakdown analysis + Key influencers)

- Dashboard file:
- `powerbi_dashboard/Uber_Trip_Analysis_Dashboard.pbix`

---

## Power BI Dashboard Screenshots

### Overview
![Dashboard Overview](PowerBi_Dashboard/dashboard_overview.png)

### Base Analysis
![Dashboard Base Analysis](PowerBi_Dashboard/ashboard_base_analysis.png)

### Prediction
![Dashboard Prediction](PowerBi_Dashboard/dashboard_prediction.png)

---

## Author 

**Aparna Patel**

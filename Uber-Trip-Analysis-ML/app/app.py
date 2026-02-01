import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------- THEME COLORS ----------
BG_COLOR        = "#F3F5FF"   # light blue background
CARD_COLOR      = "#FFFFFF"   # white cards
PRIMARY_COLOR   = "#2563EB"   # royal blue
SECONDARY_COLOR = "#F97316"   # orange accent
GREEN_COLOR     = "#16A34A"   # good / growth
RED_COLOR       = "#DC2626"   # bad / drop
TEXT_COLOR      = "#0F172A"   # dark navy text
MUTED_COLOR     = "#9CA3AF"   # grey text / borders

# Common layout for Plotly figures
plotly_layout = dict(
    paper_bgcolor=BG_COLOR,
    plot_bgcolor=CARD_COLOR,
    font=dict(color=TEXT_COLOR, family="Segoe UI, sans-serif"),
    xaxis=dict(gridcolor="#E5E7EB"),
    yaxis=dict(gridcolor="#E5E7EB"),
    legend=dict(bgcolor=CARD_COLOR, bordercolor="#E5E7EB"),
    colorway=[
        PRIMARY_COLOR,
        SECONDARY_COLOR,
        GREEN_COLOR,
        "#0EA5E9",   # extra blue
        "#A855F7"    # purple
    ]
)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Uber Trip Analytics",
    layout="wide",
    page_icon="🚕"
)

# CSS for global background + cards + metrics
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
    }}
    div[data-testid="metric-container"] {{
        background-color: {CARD_COLOR};
        padding: 16px 12px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
    }}
    section[data-testid="stSidebar"] {{
        background-color: #E0E7FF;
    }}
    h1, h2, h3, h4 {{
        color: {TEXT_COLOR};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#  LOAD DATA 
@st.cache_data
def load_data():
    df = pd.read_csv("../data/Uber-Jan-Feb-FOIL.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["day_name"] = df["date"].dt.day_name()
    df["month"] = df["date"].dt.month_name()
    return df

df = load_data()

# SIDEBAR FILTERS 
st.sidebar.title("🔍 Filters")

selected_month = st.sidebar.multiselect(
    "Select Month", df["month"].unique(), default=df["month"].unique()
)

selected_base = st.sidebar.multiselect(
    "Select Base", df["dispatching_base_number"].unique(),
    default=df["dispatching_base_number"].unique()
)

filtered_df = df[
    (df["month"].isin(selected_month)) &
    (df["dispatching_base_number"].isin(selected_base))
]

# KPI SECTION 
st.title("🚕 Uber Trip Analytics Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

total_trips = int(filtered_df["trips"].sum())
total_vehicles = int(filtered_df["active_vehicles"].sum())
peak_trips = int(filtered_df["trips"].max())
busiest_day = (
    filtered_df.groupby("day_name")["trips"].sum().idxmax()
    if not filtered_df.empty else "N/A"
)
avg_trips_per_vehicle = (
    round(total_trips / total_vehicles, 2) if total_vehicles > 0 else 0
)

col1.metric("Total Trips", f"{total_trips:,}")
col2.metric("Active Vehicles", f"{total_vehicles:,}")
col3.metric("Peak Day Trips", f"{peak_trips:,}")
col4.metric("Busiest Day", busiest_day)
col5.metric("Trips per Vehicle", avg_trips_per_vehicle)

st.markdown("---")

# DEMAND TREND
st.subheader("📈 Trip Demand Over Time")

trend_df = filtered_df.groupby("date")["trips"].sum().reset_index()
trend_df["rolling_avg"] = trend_df["trips"].rolling(7).mean()

fig_trend = go.Figure()
fig_trend.add_trace(
    go.Scatter(
        x=trend_df["date"],
        y=trend_df["trips"],
        mode="lines+markers",
        name="Daily Trips",
        line=dict(color=PRIMARY_COLOR, width=2),
        marker=dict(size=4)
    )
)
fig_trend.add_trace(
    go.Scatter(
        x=trend_df["date"],
        y=trend_df["rolling_avg"],
        mode="lines",
        name="7-Day Avg",
        line=dict(color=SECONDARY_COLOR, width=3, dash="dash")
    )
)
fig_trend.update_layout(
    **plotly_layout,
    margin=dict(l=10, r=10, t=40, b=10),
    yaxis_title="Number of Trips",
    xaxis_title="Date"
)

st.plotly_chart(fig_trend, use_container_width=True)

#  VEHICLES VS TRIPS
st.subheader("🚗 Vehicles vs Trips Relationship")

fig_scatter = px.scatter(
    filtered_df,
    x="active_vehicles",
    y="trips",
    trendline="ols",
    title="Correlation between Active Vehicles and Trips",
    template="simple_white"
)
fig_scatter.update_traces(marker=dict(color=PRIMARY_COLOR, size=7, opacity=0.7))
fig_scatter.update_layout(
    plot_bgcolor=CARD_COLOR,
    paper_bgcolor=BG_COLOR,
    font_color=TEXT_COLOR,
    xaxis_gridcolor="#E5E7EB",
    yaxis_gridcolor="#E5E7EB"
)

st.plotly_chart(fig_scatter, use_container_width=True)

#  DAY & MONTH PATTERNS 
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Trips by Day of Week")
    day_df = filtered_df.groupby("day_name")["trips"].sum().reset_index()

    if not day_df.empty:
        day_order = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
        day_df["day_name"] = pd.Categorical(
            day_df["day_name"],
            categories=day_order,
            ordered=True
        )
        day_df = day_df.sort_values("day_name")

        fig_day = px.bar(
            day_df,
            x="day_name",
            y="trips",
            color="day_name",
            color_discrete_sequence=[
                PRIMARY_COLOR, "#3B82F6", "#60A5FA",
                "#93C5FD", SECONDARY_COLOR, "#FBBF24", "#10B981"
            ],
            template="simple_white"
        )
        fig_day.update_layout(
            showlegend=False,
            plot_bgcolor=CARD_COLOR,
            paper_bgcolor=BG_COLOR,
            font_color=TEXT_COLOR,
            xaxis_gridcolor="#E5E7EB",
            yaxis_gridcolor="#E5E7EB"
        )
        st.plotly_chart(fig_day, use_container_width=True)
    else:
        st.warning("No data available for selected filters.")
        day_df = pd.DataFrame(columns=["day_name", "trips"])

with col2:
    st.subheader("🗓 Trips by Month")
    month_df = filtered_df.groupby("month")["trips"].sum().reset_index()

    if not month_df.empty:
        fig_month = px.pie(
            month_df,
            names="month",
            values="trips",
            color="month",
            color_discrete_sequence=px.colors.sequential.Blues,
            template="simple_white"
        )
        fig_month.update_layout(
            paper_bgcolor=BG_COLOR,
            font_color=TEXT_COLOR,
            showlegend=True
        )
        st.plotly_chart(fig_month, use_container_width=True)
    else:
        st.warning("No monthly data available.")

# BASE PERFORMANCE
st.subheader("🏢 Base Performance Trend")

base = st.selectbox("Select Base for Analysis", df["dispatching_base_number"].unique())

base_df = df[df["dispatching_base_number"] == base]
base_trend = base_df.groupby("date")["trips"].sum().reset_index()

fig_base = px.line(
    base_trend,
    x="date",
    y="trips",
    title=f"Trips Trend for Base {base}",
    template="simple_white"
)
fig_base.update_traces(line=dict(color=PRIMARY_COLOR, width=3))
fig_base.update_layout(
    plot_bgcolor=CARD_COLOR,
    paper_bgcolor=BG_COLOR,
    font_color=TEXT_COLOR,
    xaxis_gridcolor="#E5E7EB",
    yaxis_gridcolor="#E5E7EB"
)
st.plotly_chart(fig_base, use_container_width=True)

# SMART INSIGHTS
st.subheader("Insights")

if not day_df.empty:
    best_day = day_df.sort_values("trips", ascending=False).iloc[0]["day_name"]
    worst_day = day_df.sort_values("trips").iloc[0]["day_name"]
else:
    best_day = worst_day = "N/A"

if not month_df.empty:
    top_month = month_df.sort_values("trips", ascending=False).iloc[0]["month"]
else:
    top_month = "N/A"

st.info(
    f"""
    🔹 Trips are highest on **{best_day}** and lowest on **{worst_day}**.  
    🔹 There is a strong positive relationship between **active vehicles and trips**.  
    🔹 **{top_month}** shows the highest demand.
    """
)

# PREDICTION SECTION
st.subheader("🔮 Next 7-Day Trip Forecast")

if not trend_df.empty:
    trend_df["day_num"] = np.arange(len(trend_df))
    X = trend_df[["day_num"]]
    y = trend_df["trips"]

    model = LinearRegression()
    model.fit(X, y)

    future_days = 7
    future_X = np.arange(len(trend_df), len(trend_df) + future_days).reshape(-1, 1)
    future_preds = model.predict(future_X)

    future_dates = pd.date_range(trend_df["date"].iloc[-1], periods=future_days + 1)[1:]

    fig_forecast = go.Figure()
    fig_forecast.add_trace(
        go.Scatter(
            x=trend_df["date"],
            y=trend_df["trips"],
            name="Actual",
            mode="lines",
            line=dict(color=PRIMARY_COLOR, width=2)
        )
    )
    fig_forecast.add_trace(
        go.Scatter(
            x=future_dates,
            y=future_preds,
            name="Forecast",
            mode="lines+markers",
            line=dict(color=GREEN_COLOR, width=3, dash="dash"),
            marker=dict(size=6)
        )
    )
    fig_forecast.update_layout(
        **plotly_layout,
        yaxis_title="Trips",
        xaxis_title="Date",
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig_forecast, use_container_width=True)
else:
    st.warning("Not enough data to build forecast.")

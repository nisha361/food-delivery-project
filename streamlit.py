import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Online Food Delivery Analysis",
    layout="wide"
)

st.title("🍔 Online Food Delivery Analysis Dashboard")
st.caption("EDA • Python • Streamlit")

# ---------------------------
# LOAD DATASET
# ---------------------------
csv_path = r"C:\Users\Nishadinesh\Documents\food delivery project\ONINE_FOOD_DELIVERY_ANALYSIS.csv"

df = pd.read_csv(csv_path)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Clean key columns
df["order_status"] = df["order_status"].astype(str).str.strip().str.title()

# ---------------------------
# KPI CALCULATIONS
# ---------------------------
total_orders = len(df)
total_revenue = df["final_amount"].sum()
avg_order_value = df["order_value"].mean()
avg_delivery_time = df["delivery_time_min"].mean()
avg_rating = df["delivery_rating"].mean()

cancellation_rate = (
    len(df[df["order_status"] == "Cancelled"]) / total_orders
) * 100

# ---------------------------
# KPI DISPLAY
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹ {total_revenue:,.0f}")
col3.metric("Avg Order Value", f"₹ {avg_order_value:.2f}")
col4.metric("Avg Delivery Time", f"{avg_delivery_time:.1f} min")

col5, col6 = st.columns(2)
col5.metric("Avg Delivery Rating", f"{avg_rating:.2f}")
col6.metric("Cancellation Rate", f"{cancellation_rate:.2f}%")

st.markdown("---")

# ---------------------------
# TABS
# ---------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📅 Orders", "🏙️ Cities", "🍽️ Restaurants", "💳 Payments", "❌ Cancellations"]
)

# ---------------------------
# TAB 1: ORDERS
# ---------------------------
with tab1:
    st.subheader("Orders by Day Type")

    day_orders = df["order_day"].value_counts()

    st.bar_chart(day_orders)

    st.subheader("Monthly Revenue Trend")

    df["order_date"] = pd.to_datetime(df["order_date"])
    monthly_revenue = df.groupby(df["order_date"].dt.month)["final_amount"].sum()

    st.line_chart(monthly_revenue)

# ---------------------------
# TAB 2: CITIES
# ---------------------------
with tab2:
    st.subheader("Revenue by City")

    city_revenue = df.groupby("city")["final_amount"].sum().sort_values(ascending=False)

    st.bar_chart(city_revenue)

    st.subheader("Average Delivery Time by City")

    city_delivery = df.groupby("city")["delivery_time_min"].mean()

    st.bar_chart(city_delivery)

# ---------------------------
# TAB 3: RESTAURANTS
# ---------------------------
with tab3:
    st.subheader("Top 10 Restaurants by Rating")

    top_restaurants = (
        df.groupby("restaurant_name")["restaurant_rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(top_restaurants)

# ---------------------------
# TAB 4: PAYMENTS
# ---------------------------
with tab4:
    st.subheader("Orders by Payment Mode")

    payment_orders = df["payment_mode"].value_counts()

    st.bar_chart(payment_orders)

# ---------------------------
# TAB 5: CANCELLATIONS
# ---------------------------
with tab5:
    st.subheader("Cancellation Reasons")

    cancel_reason = (
        df[df["order_status"] == "Cancelled"]["cancellation_reason"]
        .value_counts()
    )

    st.bar_chart(cancel_reason)

    st.subheader("Cancellation Rate by Restaurant")

    cancel_rate_rest = (
        df.groupby("restaurant_name")["order_status"]
        .apply(lambda x: (x == "Cancelled").mean() * 100)
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(cancel_rate_rest)

# ---------------------------
# DATA FILTER
# ---------------------------
st.markdown("---")
st.subheader("🔍 Filter Orders by Status")

status = st.selectbox(
    "Select Order Status",
    df["order_status"].unique()
)

filtered_df = df[df["order_status"] == status]
st.dataframe(filtered_df)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown("**End-to-End Project | Python • Streamlit • EDA**")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    layout="wide"
)

# ======================
# LOAD DATA
# ======================

df = pd.read_csv('main_data.csv')

# ======================
# TITLE
# ======================

st.title("📊 Olist E-Commerce Dashboard")

st.markdown("""
Dashboard ini digunakan untuk menganalisis performa penjualan pada platform Olist.
""")

# ======================
# KPI
# ======================

total_orders = df['order_id'].nunique()
total_revenue = df['price'].sum()
average_price = df['price'].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Orders",
        value=total_orders
    )

with col2:
    st.metric(
        label="Total Revenue",
        value=f"${total_revenue:,.2f}"
    )

with col3:
    st.metric(
        label="Average Product Price",
        value=f"${average_price:,.2f}"
    )

# ======================
# TOP PRODUCT CATEGORY
# ======================

st.subheader("Top 10 Product Categories by Revenue")

sales_per_category = df.groupby(
    'product_category_name_english'
)['price'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,5))

sales_per_category.plot(
    kind='bar',
    color='skyblue',
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

# ======================
# MONTHLY ORDER TREND
# ======================

st.subheader("Monthly Orders Trend")

df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

df['order_month'] = df[
    'order_purchase_timestamp'
].dt.to_period('M').astype(str)

monthly_orders = df.groupby(
    'order_month'
)['order_id'].nunique()

fig2, ax2 = plt.subplots(figsize=(12,5))

monthly_orders.plot(
    kind='line',
    marker='o',
    color='orange',
    ax=ax2
)

plt.xticks(rotation=45)

st.pyplot(fig2)

# ======================
# DATA PREVIEW
# ======================

st.subheader("Dataset Preview")

st.dataframe(df.head())
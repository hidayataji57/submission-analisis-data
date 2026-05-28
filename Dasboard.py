import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# PAGE CONFIG

st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    layout="wide"
)

# LOAD DATA

df = pd.read_csv('main_data.csv')

# CONVERT DATETIME

df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

# SIDEBAR

st.sidebar.header("Filter Dashboard")

# FILTER TANGGAL

min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date]
)

# FILTER KATEGORI

category_filter = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=df['product_category_name_english'].dropna().unique(),
    placeholder="Pilih kategori produk"
)

# FILTER KOTA

city_filter = st.sidebar.multiselect(
    "Pilih Kota",
    options=df['customer_city'].dropna().unique(),
    placeholder="Pilih kota"
)

# FILTER DATAFRAME

filtered_df = df.copy()

# FILTER KATEGORI

if category_filter:
    filtered_df = filtered_df[
        filtered_df['product_category_name_english'].isin(category_filter)
    ]

# FILTER KOTA

if city_filter:
    filtered_df = filtered_df[
        filtered_df['customer_city'].isin(city_filter)
    ]

# FILTER TANGGAL

filtered_df = filtered_df[
    (filtered_df['order_purchase_timestamp'].dt.date >= start_date) &
    (filtered_df['order_purchase_timestamp'].dt.date <= end_date)
]

# TITLE

st.title("📊 Olist E-Commerce Dashboard")

st.markdown("""
Dashboard ini digunakan untuk menganalisis performa penjualan pada platform Olist.
""")

# KPI

total_orders = filtered_df['order_id'].nunique()
total_revenue = filtered_df['price'].sum()
average_price = filtered_df['price'].mean()

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

# TOP CATEGORY

st.subheader("Top 10 Product Categories by Revenue")

sales_per_category = filtered_df.groupby(
    'product_category_name_english'
)['price'].sum().sort_values(ascending=False).head(10)

fig = px.bar(
    sales_per_category,
    x=sales_per_category.index,
    y=sales_per_category.values,
    labels={'x': 'Category', 'y': 'Revenue'},
    color=sales_per_category.values
)

st.plotly_chart(fig, use_container_width=True)

# MONTHLY TREND

st.subheader("Monthly Orders Trend")

filtered_df['order_month'] = filtered_df[
    'order_purchase_timestamp'
].dt.to_period('M').astype(str)

monthly_orders = filtered_df.groupby(
    'order_month'
)['order_id'].nunique().reset_index()

fig2 = px.line(
    monthly_orders,
    x='order_month',
    y='order_id',
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# TOP CUSTOMER CITY

st.subheader("Top 10 Customer Cities")

top_city = filtered_df['customer_city'].value_counts().head(10)

fig3 = px.pie(
    values=top_city.values,
    names=top_city.index,
    title="Customer Distribution by City"
)

st.plotly_chart(fig3, use_container_width=True)

# DOWNLOAD FILTERED DATA

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)

# SHOW DATA

if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
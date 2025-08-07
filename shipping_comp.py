import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Excel Insights Dashboard", layout="wide")

st.title("📊 Excel Data Insights Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name='Sheet1')

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # ----- Summary Statistics -----
    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe(include='all'))

    # ----- Missing Values -----
    st.subheader("❗ Missing Values")
    missing = df.isnull().sum()
    st.dataframe(missing[missing > 0].to_frame(name="Missing Count"))

    # ----- Correlation Matrix -----
    st.subheader("📌 Correlation Matrix (Numerical Columns)")
    corr = df.corr(numeric_only=True)
    fig_corr, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig_corr)

    # ----- Region Summary -----
    st.subheader("🌍 Sales & Profit by Region")
    region_summary = df.groupby("Region")[["Sales", "Profit", "Order Quantity"]].sum().sort_values(by="Sales", ascending=False)
    st.dataframe(region_summary)

    fig_region = px.bar(
        region_summary.reset_index(),
        x="Region", y="Sales",
        color="Region",
        title="Total Sales by Region",
        labels={"Sales": "Total Sales"}
    )
    st.plotly_chart(fig_region)

    # ----- Order Priority Pie Chart -----
    st.subheader("🧩 Order Priority Distribution")
    priority_counts = df['Order Priority'].value_counts()
    fig_priority = px.pie(
        names=priority_counts.index,
        values=priority_counts.values,
        title="Order Priority Breakdown",
    )
    st.plotly_chart(fig_priority)

    # ----- Top 10 Products by Sales -----
    st.subheader("🏆 Top 10 Products by Sales")
    top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
    st.dataframe(top_products)

    fig_top = px.bar(
        top_products.sort_values().reset_index(),
        x="Sales", y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        color="Sales"
    )
    st.plotly_chart(fig_top)

    # ----- Profit by Category/Sub-category -----
    st.subheader("📦 Profit by Category & Sub-Category")
    category_profit = df.groupby(["Product Category", "Product Sub-Category"])["Profit"].sum().reset_index()
    fig_cat = px.bar(
        category_profit,
        x="Profit", y="Product Sub-Category",
        color="Product Category",
        title="Profit by Category & Sub-Category",
        orientation='h',
        height=600
    )
    st.plotly_chart(fig_cat)

    st.success("✅ Dashboard updated with insights and charts!")

else:
    st.info("⬆️ Upload an Excel file to explore insights.")

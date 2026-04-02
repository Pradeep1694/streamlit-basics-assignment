import streamlit as st
import pandas as pd

st.title("Sales App")
st.write("Welcome to the sales app! Track the sales and analyze the data")
st.write(f"The current time is: {__import__('datetime').datetime.now()}")
st.subheader("sales summary")

data = {
    "Product": ["samsung", "iPhone", "oppo", "Headphones", "Monitor", "Televison", "Refrigerator"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories","Home Appliances", "Home Appliances"],
    "Sales": [150000, 120000, 20000, 10000, 15000, 25000, 35000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.title("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter DataFrame
filtered_df = df[df["Category"] == category]

# Display filtered data
st.write("Filtered Sales Data")
st.dataframe(filtered_df)

# Line chart
st.write("Sales Trend")
st.line_chart(filtered_df["Sales"])

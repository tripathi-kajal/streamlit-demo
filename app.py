import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚀 My First Streamlit App with Features")

# --- Text input & slider ---
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old! 🎉")

# --- Table Example ---
st.subheader("📊 Sample Table")
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 29],
    "City": ["New York", "London", "Paris"]
})
st.table(data)

# --- Chart Example ---
st.subheader("📈 Sample Chart")
chart_data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 15, 25, 30]
})
st.line_chart(chart_data.set_index("x"))

# --- File Upload ---
st.subheader("📂 Upload a CSV File")
uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ File uploaded successfully!")
    st.dataframe(df)

    # Simple chart from uploaded file
    st.bar_chart(df.select_dtypes(include="number"))

import streamlit as st
import pandas as pd
import numpy as np

st.title("🚀 My First Streamlit App with Extra Features")

# --- Form section ---
st.header("📝 User Form")
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old! 🎉")

# --- Chart section ---
st.header("📊 Random Data Chart")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(data)

# --- Table section ---
st.header("📋 Sample Table")
table_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 29],
    "City": ["New York", "London", "Paris"]
}
st.table(pd.DataFrame(table_data))

# --- File upload section ---
st.header("📂 Upload Your CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully ✅")
    st.write("Here’s a preview of your data:")
    st.dataframe(df)

import streamlit as st

st.title("🚀 My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Slider
age = st.slider("Select your age:", 1, 100, 25)

# Button
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old! 🎉")

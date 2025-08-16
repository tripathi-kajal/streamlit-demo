import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import random

# -------------------------------
# 🚀 My First Streamlit App
# -------------------------------
st.title("🚀 My First Streamlit App")

# Name & Age
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

if name:
    st.success(f"Hello {name}, you are {age} years old! 🎉")

# -------------------------------
# 📊 Chart Section
# -------------------------------
st.subheader("📊 A Simple Chart")
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="Sine wave", color="blue")
ax.legend()
st.pyplot(fig)

# -------------------------------
# 📂 File Upload (CSV)
# -------------------------------
st.subheader("📂 Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Here’s a preview of your data:")
    st.dataframe(df)

# -------------------------------
# 🖼️ Image Upload
# -------------------------------
st.subheader("🖼️ Upload an Image")
image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if image_file:
    img = Image.open(image_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

# -------------------------------
# 🎲 Fun Button (Jokes/Facts)
# -------------------------------
st.subheader("🎲 Fun Zone")
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything! 😂",
    "Did you know? Honey never spoils 🍯",
    "Fun fact: Octopuses have three hearts 🐙",
]

if st.button("Tell me something fun 🎲"):
    st.success(random.choice(jokes))

# -------------------------------
# 🌈 Sidebar Settings
# -------------------------------
st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Choose a theme:", ["Light", "Dark", "Colorful"])
if theme == "Dark":
    st.write("🌑 Dark mode activated!")
elif theme == "Colorful":
    st.write("🌈 Yay! Colors everywhere!")
else:
    st.write("☀️ Light mode is peaceful.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------------
# ⚡ Tripathi Electricals
# -------------------------------
st.title("⚡ Tripathi Electricals")
st.write("Welcome to **Tripathi Electricals** – Reliable services for all your electrical needs!")

# -------------------------------
# 📋 Services Offered
# -------------------------------
st.subheader("📋 Our Services")
services = [
    "Wiring",
    "Repairs",
    "Solar Installation",
    "Maintenance",
    "Other (custom work)"
]

for s in services:
    st.markdown(f"✅ **{s}**")

# -------------------------------
# 💰 Pricing Info
# -------------------------------
st.subheader("💰 Pricing")
st.write("💡 Pricing depends on the type of work. Contact us for a free estimate!")

# -------------------------------
# 📈 Example Chart (Service Trends)
# -------------------------------
st.subheader("📈 Example: Service Request Trends")
months = ["Jan", "Feb", "Mar", "Apr", "May"]
requests = [10, 20, 15, 25, 30]

fig, ax = plt.subplots()
ax.plot(months, requests, marker="o", color="orange")
ax.set_ylabel("Number of Requests")
ax.set_title("Monthly Service Requests")
st.pyplot(fig)

# -------------------------------
# 📝 Contact / Service Request Form
# -------------------------------
st.subheader("📝 Book a Service")
with st.form("service_form"):
    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    service_type = st.selectbox("Select Service", services)
    details = st.text_area("Additional Details (optional)")
    submitted = st.form_submit_button("Submit Request")
    if submitted:
        st.success(f"✅ Thank you {name}! We’ll contact you at {phone} for {service_type}.")

# -------------------------------
# 📂 Upload Problem Details / Photos
# -------------------------------
st.subheader("📂 Upload Details or Photos")
uploaded_file = st.file_uploader("Upload a file (image or document)", type=["jpg", "png", "jpeg", "pdf"])
if uploaded_file:
    if uploaded_file.type.startswith("image/"):
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Issue", use_column_width=True)
    else:
        st.write("📄 File uploaded:", uploaded_file.name)

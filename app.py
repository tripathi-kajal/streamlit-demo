import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
import smtplib
from email.mime.text import MIMEText

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
# 📞 Business Contact
# -------------------------------
st.subheader("📞 Contact Us")
st.markdown("""
For queries, reach out at:  
📧 **rajeshtripathi911@gmail.com**  
📱 Phone: +91-XXXXXXXXXX
""")

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
# 📧 Email Notification Function
# -------------------------------
def send_email_notification(subject, body):
    sender = "your_email@gmail.com"          # your Gmail
    password = "your_app_password"           # Gmail App Password
    recipient = "rajeshtripathi911@gmail.com" # Business email

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        st.success("📧 Email notification sent successfully!")
    except Exception as e:
        st.error(f"Email failed: {e}")

# -------------------------------
# 📝 Service Request Form
# -------------------------------
st.subheader("📝 Book a Service")

DATA_FILE = "service_requests.csv"

def save_request(name, phone, service_type, details):
    new_data = pd.DataFrame([{
        "Name": name,
        "Phone": phone,
        "Service": service_type,
        "Details": details
    }])

    if os.path.exists(DATA_FILE):
        existing = pd.read_csv(DATA_FILE)

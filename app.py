import streamlit as st
import matplotlib.pyplot as plt

# App title
st.title("⚡ Tripathi Electricals")

st.write(
    "Welcome to **Tripathi Electricals**! We provide reliable and affordable "
    "electrical services including wiring, repairs, solar installation, and maintenance."
)

# Services
st.header("🔧 Services Offered")
st.write("""
- Wiring  
- Electrical Repairs  
- Solar Installation  
- Maintenance  
""")

# Pricing
st.header("💰 Pricing")
st.write("Pricing depends on the type of work. Contact us for a detailed quote.")

# Business email
st.info("📧 For queries, reach us at: **rajeshtripathi911@gmail.com**")

# File upload
st.header("📎 Upload Issue Photos/Details")
uploaded_file = st.file_uploader("Upload a file (optional):", type=["jpg", "png", "pdf"])
if uploaded_file:
    st.success("✅ File uploaded successfully!")

# Chart example
st.header("📊 Service Request Trends (Demo Data)")
services = ["Wiring", "Repairs", "Solar", "Maintenance"]
counts = [15, 30, 10, 20]

fig, ax = plt.subplots()
ax.bar(services, counts)
ax.set_ylabel("Number of Requests")
st.pyplot(fig)

# Tabs for forms
st.header("📬 Contact & Booking")

tab1, tab2 = st.tabs(["📑 Book a Service", "📝 Ask a Query"])

with tab1:
    st.subheader("Book a Service")
    with st.form("service_form"):
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        service_required = st.selectbox(
            "Service Required",
            ["Wiring", "Repairs", "Solar Installation", "Maintenance"]
        )
        submit = st.form_submit_button("Submit Request")
        if submit:
            st.success(f"✅ Thank you {name}! We will contact you at {phone} for {service_required} service.")

with tab2:
    st.subheader("📝 Get in Touch")
    with st.form("query_form"):
        q_name = st.text_input("Your Name")
        q_email = st.text_input("Your Email")
        q_message = st.text_area("Your Query")
        q_submit = st.form_submit_button("Send Query")
        if q_submit:
            st.success(f"✅ Thank you {q_name}! We will reply to you at {q_email} soon.")

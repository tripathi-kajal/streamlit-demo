# -------------------------------
# 📝 Forms Section
# -------------------------------
st.subheader("📝 Get in Touch")

tab1, tab2 = st.tabs(["📋 Book a Service", "💬 Ask a Query"])

# -------- Service Request Form --------
with tab1:
    st.markdown("Fill in details to request an electrical service:")

    with st.form("service_form"):
        name = st.text_input("Your Name")
        phone = st.text_input("Phone Number")
        service_type = st.selectbox("Select Service", services)
        details = st.text_area("Additional Details (optional)")
        submitted = st.form_submit_button("Submit Request")

        if submitted:
            save_request(name, phone, service_type, details)
            send_email_notification(
                f"New Service Request from {name}",
                f"Name: {name}\nPhone: {phone}\nService: {service_type}\nDetails: {details}"
            )
            st.success(f"✅ Thank you {name}! We’ll contact you at {phone} for {service_type}.")

# -------- General Query Form --------
with tab2:
    st.markdown("Have a question? Submit your query here:")

    with st.form("query_form"):
        q_name = st.text_input("Your Name")
        q_email = st.text_input("Your Email")
        q_phone = st.text_input("Phone Number")
        q_text = st.text_area("Your Query")
        q_submitted = st.form_submit_button("Submit Query")

        if q_submitted:
            save_query(q_name, q_email, q_phone, q_text)
            send_email_notification(
                f"New Query from {q_name}",
                f"Name: {q_name}\nEmail: {q_email}\nPhone: {q_phone}\nQuery: {q_text}"
            )
            st.success("✅ Thank you! We’ll get back to you soon.")

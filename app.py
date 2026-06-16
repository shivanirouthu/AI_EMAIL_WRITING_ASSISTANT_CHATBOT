import streamlit as st
from main import generate_email

st.set_page_config(
    page_title="AI Email Writing Assistant",
    page_icon="📧"
)

st.title("📧 AI Email Writing Assistant")

email_request = st.text_area(
    "Enter your email request",
    placeholder="Example: Write a leave email for 2 days due to fever"
)

if st.button("Generate Email", key="generate_btn"):

    if not email_request.strip():
        st.warning("Please enter an email request.")
    else:
        try:
            result = generate_email(email_request)

            st.subheader("Generated JSON Output")
            st.json(result.model_dump())

        except Exception as e:
            st.error(f"Error: {str(e)}")
import streamlit as st

from main import generate_email

st.title(
    "AI Email Writing Assistance Chatbot"
)

email_request = st.text_area(
    "Describe your email"
)

if st.button("Generate Email"):

    result = generate_email(
        email_request
    )

    st.subheader("Subject")
    st.write(result.subject)

    st.subheader("Email")
    st.write(result.email_body)

    st.subheader("Tone")
    st.write(result.tone)
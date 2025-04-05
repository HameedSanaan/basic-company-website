import streamlit as st
import pandas as pd
from send_email import send_email
df = pd.read_csv("topics.csv")
st.header("Contact Us")

with st.form(key='my_form'):
    email = st.text_input('Your Email Address')
    selection = st.selectbox(
        "What topic would you like to discuss?",
        (df)
    )
    raw_message = st.text_area("Text")
    message = f"""\
Subject: {selection}

From: {email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Email sent")

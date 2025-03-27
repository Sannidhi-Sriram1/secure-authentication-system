import streamlit as st
from auth import register_user, login_user, reset_password, update_password
import os

# Set page title and layout
st.set_page_config(page_title="🔐 Secure Authentication", layout="centered")

# Apply custom styling
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { background-color: #4CAF50; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    .stSelectbox>div>div { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Session Management
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None

# Sidebar Navigation
menu = st.sidebar.radio("🔍 Navigation", ["Login", "Register", "Reset Password"])

if menu == "Login":
    st.title("🔑 Login")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("Login"):
        success, message = login_user(username, password)
        if success:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login Successful!")
        else:
            st.error("❌ " + message)

elif menu == "Register":
    st.title("📝 Register")

    username = st.text_input("👤 Choose a Username")
    password = st.text_input("🔒 Set a Password", type="password")
    email = st.text_input("📧 Enter Your Email")

    if st.button("Register"):
        message = register_user(username, password, email)
        if "✅" in message:
            st.success(message)
        else:
            st.error(message)

elif menu == "Reset Password":
    st.title("🔄 Reset Password")

    username = st.text_input("👤 Enter Your Username")
    email = st.text_input("📧 Enter Your Registered Email")

    if st.button("Send OTP"):
        otp_message = reset_password(username, email)
        if "✅" in otp_message:
            st.session_state.otp_sent = True
            st.session_state.reset_username = username
            st.success(otp_message)
        else:
            st.error(otp_message)

    # OTP Verification Section
    if st.session_state.get("otp_sent", False):
        otp_input = st.text_input("🔢 Enter OTP Sent to Email")
        new_password = st.text_input("🔒 Enter New Password", type="password")

        if st.button("Reset Password"):
            message = update_password(st.session_state.reset_username, otp_input, new_password)
            if "✅" in message:
                st.success(message)
                st.session_state.otp_sent = False  # Reset session state
            else:
                st.error(message)

import streamlit as st
from auth import register_user, login_user, reset_password, get_user_secret
from session_manager import is_authenticated, logout
import pyotp
import qrcode
from PIL import Image
import os

st.set_page_config(page_title="Secure Authentication System", layout="centered")

# Ensure the QR code directory exists
QR_DIR = "qrcodes"
if not os.path.exists(QR_DIR):
    os.makedirs(QR_DIR)

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

st.title("🔒 Secure Authentication System")

menu = ["Register", "Login", "Reset Password", "Logout"]
choice = st.sidebar.selectbox("Navigation", menu)

# Registration
if choice == "Register":
    st.subheader("Register a New User")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    email = st.text_input("Enter Email (for password recovery)")

    if st.button("Register"):
        secret, qr_path = register_user(username, password, email)
        if secret:
            st.success("Registration Successful! Scan this QR Code for MFA:")
            st.image(qr_path)
        else:
            st.error("User already exists!")

# Login
elif choice == "Login":
    st.subheader("User Login")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        user_data = login_user(username, password)
        if user_data:
            secret = get_user_secret(username)
            if secret:
                otp = st.text_input("Enter OTP from Authenticator", type="password")
                totp = pyotp.TOTP(secret)
                if totp.verify(otp):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.success(f"Welcome {username}! You are logged in.")
                else:
                    st.error("Invalid OTP! Try again.")
            else:
                st.error("MFA Secret not found. Contact support.")
        else:
            st.error("Invalid Credentials!")

# Password Reset
elif choice == "Reset Password":
    st.subheader("Reset Your Password")
    username = st.text_input("Enter Username")
    email = st.text_input("Enter Registered Email")

    if st.button("Send Reset OTP"):
        if reset_password(username, email):
            st.success("Check your email for OTP to reset your password.")

# Logout
elif choice == "Logout":
    logout()
    st.success("You have been logged out.")


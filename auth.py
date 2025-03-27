import bcrypt
import json
import os
import random
from otp_service import send_otp

USER_FILE = "users.json"
OTP_FILE = "otp.json"


# Load user data
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as file:
        return json.load(file)


# Save user data
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)


# Load OTP data
def load_otps():
    if not os.path.exists(OTP_FILE):
        return {}
    with open(OTP_FILE, "r") as file:
        return json.load(file)


# Save OTP data
def save_otps(otps):
    with open(OTP_FILE, "w") as file:
        json.dump(otps, file)


# Register user
def register_user(username, password, email):
    users = load_users()

    if username in users:
        return "❌ Username already exists!"

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = {"password": hashed_password, "email": email}
    save_users(users)
    return "✅ Registration successful!"


# Login user
def login_user(username, password):
    users = load_users()

    if username not in users:
        return False, "❌ User not found!"

    stored_password = users[username]["password"]
    if bcrypt.checkpw(password.encode(), stored_password.encode()):
        return True, "✅ Login successful!"
    else:
        return False, "❌ Incorrect password!"


# Send OTP for password reset
def reset_password(username, email):
    users = load_users()
    if username not in users or users[username]["email"] != email:
        return "❌ User not found or email does not match!"

    otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
    otps = load_otps()
    otps[username] = otp
    save_otps(otps)

    send_otp(email, otp)
    return f"✅ OTP sent to {email}. Enter the OTP to reset your password."


# Update password after OTP verification
def update_password(username, otp, new_password):
    users = load_users()
    otps = load_otps()

    if username not in users:
        return "❌ User not found!"

    if username not in otps or otps[username] != otp:
        return "❌ Invalid OTP!"

    hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
    users[username]["password"] = hashed_password
    save_users(users)

    del otps[username]  # Remove used OTP
    save_otps(otps)

    return "✅ Password reset successful! You can now log in with your new password."

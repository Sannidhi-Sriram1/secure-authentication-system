import bcrypt
import json
import pyotp
import os
import qrcode
from PIL import Image

USER_DB = "users.json"
QR_DIR = "qrcodes"

if not os.path.exists(USER_DB):
    with open(USER_DB, "w") as file:
        json.dump({}, file)

if not os.path.exists(QR_DIR):
    os.makedirs(QR_DIR)

# Load user data
def load_users():
    with open(USER_DB, "r") as file:
        return json.load(file)

# Save user data
def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file, indent=4)

# Register User
def register_user(username, password, email):
    users = load_users()

    if username in users:
        return None, None  # User already exists

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Generate MFA Secret
    secret = pyotp.random_base32()

    # Generate QR Code
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="SecureAuthSystem")
    qr_path = f"{QR_DIR}/{username}_qr.png"
    qr = qrcode.make(uri)
    qr.save(qr_path)

    # Store user data
    users[username] = {"password": hashed_password, "email": email, "secret": secret}
    save_users(users)

    return secret, qr_path

# Login User
def login_user(username, password):
    users = load_users()

    if username in users and bcrypt.checkpw(password.encode(), users[username]["password"].encode()):
        return users[username]
    return None

# Retrieve MFA Secret
def get_user_secret(username):
    users = load_users()
    return users[username]["secret"] if username in users else None

# Reset Password
def reset_password(username, email):
    users = load_users()

    if username in users and users[username]["email"] == email:
        otp = pyotp.TOTP(pyotp.random_base32()).now()
        print(f"Reset OTP for {username}: {otp}")  # Simulate email sending
        return True
    return False

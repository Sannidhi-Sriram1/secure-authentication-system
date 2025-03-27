import smtplib
from email.message import EmailMessage

# Email credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"  # Replace with your email
SENDER_PASSWORD = "your-app-password"  # Replace with your generated app password

def send_otp(receiver_email, otp):
    msg = EmailMessage()
    msg.set_content(f"Your OTP for password reset is: {otp}")
    msg["Subject"] = "Secure Authentication System - OTP Verification"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"OTP sent to {receiver_email}")
    except Exception as e:
        print("Failed to send email:", e)

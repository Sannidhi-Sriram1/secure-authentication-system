Secure Authentication Module

Overview

This project is a Secure Authentication Module designed to enhance system security. It supports multi-factor authentication (MFA) and protects against common vulnerabilities like buffer overflows and trapdoors.

Features

✅ User Registration & Login
✅ Password Reset with Email OTP
✅ Multi-Factor Authentication (MFA) using Google Authenticator
✅ Session Management (Keeps users logged in)
✅ Protection Against Buffer Overflows & Trapdoors

Technology Stack

Programming Language: Python
Framework: Streamlit
Libraries: bcrypt, pyotp, qrcode, pillow, smtplib, json
Installation

Clone the Repository:
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Create and Activate Virtual Environment:
conda create --name auth_system python=3.10 -y
conda activate auth_system
Install Dependencies:
pip install -r requirements.txt
Run the Application:
streamlit run app.py
Usage

Register with a username, password, and email.
Scan the QR Code in Google Authenticator for MFA.
Login using your password and OTP from the authenticator app.
Reset Password if needed via email OTP.
Future Improvements

🚀 OS-Level Integration (Planned)
🔒 More Advanced Security Measures

Contributors
Sriram
Your Name
License

This project is licensed under the MIT License.

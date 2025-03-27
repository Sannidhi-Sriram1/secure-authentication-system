import bcrypt

def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed_password):
    """Verify a password against a stored bcrypt hash."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

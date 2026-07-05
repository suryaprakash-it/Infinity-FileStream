import secrets
import hashlib
from datetime import datetime


def generate_file_code():
    """Generate a unique file code."""
    return secrets.token_urlsafe(8)


def generate_hash(text: str):
    """Generate SHA256 hash."""
    return hashlib.sha256(text.encode()).hexdigest()


def get_timestamp():
    """Return current UTC timestamp."""
    return datetime.utcnow()
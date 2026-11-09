import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(PROJECT_ROOT / ".env")

GMAIL_URL = "https://workspace.google.com/intl/iw/gmail/"

GMAIL_EMAIL = os.getenv("GMAIL_EMAIL", "").strip()

GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD", "").strip()

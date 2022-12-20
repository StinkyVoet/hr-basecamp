from dotenv import load_dotenv
import os

config = None

if load_dotenv(".env"):
    config = os.environ.copy()

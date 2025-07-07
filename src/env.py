import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
MODEL_NAME = os.getenv("MODEL_NAME")

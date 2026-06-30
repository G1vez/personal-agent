from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("TICKTICK_CLIENT_ID")
CLIENT_SECRET = os.getenv("TICKTICK_CLIENT_SECRET")
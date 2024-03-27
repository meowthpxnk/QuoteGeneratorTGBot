import os

from dotenv import load_dotenv
load_dotenv()


class RootSettings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    NINJAS_KEY = os.getenv("NINJAS_KEY")
    UNSPLASH_KEY = os.getenv("UNSPLASH_KEY")
    MONGO_DB_URL = os.getenv("MONGO_DB_URL")
    
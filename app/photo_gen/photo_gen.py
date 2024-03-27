import random

from app import settings
from app.utils.requests import request


class RandomPhotoGenerator:
    @staticmethod
    async def generate(query):
        res = await request(f"https://api.unsplash.com/search/photos?query={query}&client_id={settings.UNSPLASH_KEY}")
        return random.choice(res["results"])["urls"]["regular"]
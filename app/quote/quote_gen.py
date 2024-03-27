from app.utils.requests import request

from app import settings

from .emojies import EmojiManager


class Quote:
    def __init__(
            self,
            quote: str,
            category: str,
            author: str,
            emoji: str
    ):
        self.quote = quote
        self.category = category
        self.author = author
        self.emoji = emoji


class QuoteGenerator:
    def __init__(self, emoji_manager: EmojiManager):
        self.emoji_manager = emoji_manager

    @staticmethod
    async def request():

        attempts = 20

        while attempts:
            try:
                response = await request(
                    "https://api.api-ninjas.com/v1/quotes",
                    headers={"X-Api-Key": settings.NINJAS_KEY}
                )
            except:
                print("ERROED NINJAS")
                pass
            else:
                return response[0]
            finally:
                attempts -= 1

        raise Exception("Cant connect ninjas api.")

    async def generate(self):
        response = await self.request()

        quote = response.get("quote")
        category = response.get("category")
        author = response.get("author")
        emoji = self.emoji_manager(category)

        return Quote(
            quote,
            category,
            author,
            emoji,
        )


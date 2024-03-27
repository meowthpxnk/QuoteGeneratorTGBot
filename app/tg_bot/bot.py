from aiogram import Bot

from .quote_message import NewQuoteMessage


class Bot(Bot):
    
    async def send_quote(self, chat_id, quoted_message=None):

        if not quoted_message:
            quoted_message = await NewQuoteMessage.generate()

        await self.send_photo(
            chat_id,
            **quoted_message.prepare(),
        )
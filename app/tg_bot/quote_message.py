from aiogram import html

from app.translates import Translator
from app.photo_gen import RandomPhotoGenerator
from app import quote_gen

class NewQuoteMessage:
    def __init__(self, caption, photo):
        self.caption = caption
        self.photo = photo
    
    def prepare(self):
        return {
            "caption": self.caption,
            "photo": self.photo,
            "parse_mode": "html"
        }
    
    @classmethod
    async def generate(cls):
        quote_object = await quote_gen.generate()
        photo = await RandomPhotoGenerator.generate(
            quote_object.quote
        )
        ru_txt = await Translator.force_translate_text(
            quote_object.quote
        )
        caption = "\n".join([
            f"{html.blockquote(f"{quote_object.quote}\n\n{html.spoiler(ru_txt)}")}",
            f"<i><b>{quote_object.author}</b></i> {quote_object.emoji}"
        ])

        return cls(caption, photo)
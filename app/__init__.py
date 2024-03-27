#----------------------------------------

import asyncio
loop = asyncio.get_event_loop()

#----------------------------------------

from .settings import RootSettings
settings = RootSettings()

#----------------------------------------

import json
from .quote import EmojiManager, QuoteGenerator

with open("static/emojies.json", "r", encoding="utf-8") as file:
    emojies_dict = json.loads(file.read())

emoji_manager = EmojiManager(emojies_dict)
quote_gen = QuoteGenerator(emoji_manager)

#----------------------------------------

from pymongo import MongoClient
from .db import UsersDB

mongo_cl = MongoClient(settings.MONGO_DB_URL)
db = mongo_cl["MeowthLingoDB"]
users_db = UsersDB(db, "tg_users")

#----------------------------------------

from aiogram import Dispatcher
from .tg_bot.bot import Bot

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()

from .tg_bot import handlers
loop.create_task(dp.start_polling(bot))

#----------------------------------------

from .task_manager.tasks import generateNewTasks
loop.create_task(generateNewTasks())
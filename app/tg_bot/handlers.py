from aiogram.filters import CommandStart
from aiogram.types import Message

from app import dp, bot, users_db


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if users_db.exist(message.chat.id):
        await message.answer("You are already registered. Wait for new quotes ❤️")
        return
    
    users_db.registrate(message.chat.id)

    await message.answer("You has been registered. Take your personal quote ❤️")
    
    await bot.send_quote(message.chat.id)
    
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from core.loader import dp
from filters import IsGroup


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = [
        "Hello, everyone!",
        "I am screen bot. Just send me a link to get screenshot of your page!",
    ]
    await message.answer("\n".join(text))

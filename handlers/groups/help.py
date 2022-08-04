from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from core.loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        f"Hello, everyone!" f"I am screen bot. Just send me a link to get screenshot of your page!"
    ]
    await message.answer("\n".join(text))

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from core.loader import dp
from filters import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}!\n"
        f"I am screen bot. Just send me a link to get screenshot of your page!"
    )

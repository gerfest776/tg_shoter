from aiogram import types
from aiogram.types import ParseMode
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic
from aiogram.dispatcher.filters.builtin import CommandStart

from core.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f'Hello, {message.from_user.full_name}!\n'
        f'I am screen bot. Just send me a link to get screenshot of your page!'
    )

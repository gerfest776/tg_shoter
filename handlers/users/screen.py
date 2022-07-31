import validators
from aiogram import types
from aiogram.types import ParseMode
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic
from aiogram.dispatcher.filters.builtin import CommandStart

from core.loader import dp


@dp.message_handler(content_types=ContentType.TEXT)
async def link_message(msg: types.Message):
    if not validators.url(msg.text):
        await msg.reply("Please, send correct url", parse_mode=ParseMode.MARKDOWN)

from aiogram import types
from aiogram.types.message import ContentType

from core.loader import dp
from handlers.screen import handle_link_message


@dp.message_handler(commands=["screen"], content_types=ContentType.TEXT)
async def handle_link_message_groups(msg: types.Message):
    msg.text = msg.text.split(" ")[1]
    await handle_link_message(msg)

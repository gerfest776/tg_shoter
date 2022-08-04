from aiogram import types
from aiogram.types.message import ContentType

from core.loader import dp
from filters import IsPrivate
from handlers.screen import handle_link_message


@dp.message_handler(IsPrivate(), content_types=ContentType.TEXT)
async def handle_link_message_users(msg: types.Message):
    await handle_link_message(msg)

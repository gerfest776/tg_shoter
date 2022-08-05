import validators
from aiogram import types
from aiogram.types.message import ContentType, ParseMode

from core.loader import dp
from filters import IsPrivate
from handlers.screen import handle_link_message
from handlers.users.buttons import reply_help_button


@dp.message_handler(IsPrivate(), content_types=ContentType.TEXT)
async def handle_link_message_users(msg: types.Message):
    if not validators.url(msg.text):
        await msg.reply(
            "Please, send correct url",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_help_button,
        )
    else:
        await handle_link_message(msg)

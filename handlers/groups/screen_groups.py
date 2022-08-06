import validators
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.message import ContentType, ParseMode

from core.loader import dp
from filters import IsGroup
from handlers.screen import handle_link_message


@dp.message_handler(IsGroup(), commands=["screen"], content_types=ContentType.TEXT)
async def handle_link_message_groups(msg: types.Message):
    msg.text = msg.text.split(" ")[1]
    if not validators.url(msg.text):
        reply_markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(text="What i am able to?", callback_data="help_in_groups")
        )
        await msg.reply(
            "Please, send correct url", parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup
        )
    else:
        await handle_link_message(msg)


@dp.callback_query_handler(text="help_in_groups")
async def get_whois_of_page(query: CallbackQuery):
    await query.answer(
        text="Just send me a link to get screenshot of your page!\nUse: /screen *url*",
        show_alert=True,
    )

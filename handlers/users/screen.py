import validators
from aiogram import types
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
    InputMedia,
    ParseMode,
)
from aiogram.types.message import ContentType

from core.db.db_api import whois_table
from core.loader import dp
from utils.screenshot_page import Screener


@dp.message_handler(content_types=ContentType.TEXT)
async def handle_link_message(msg: types.Message):
    if not validators.url(msg.text):
        await msg.reply("Please, send correct url", parse_mode=ParseMode.MARKDOWN)
    else:
        mess = await msg.answer_photo(
            types.InputFile("./media/1x1.png"), "Your image is processing..."
        )
        reply_markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(text="Page WHOIS", callback_data="page_details_users")
        )
        file = InputMedia(
            media=InputFile(await Screener(msg.text).screen_page()),
            caption=f"Your screenshot!\n\n{msg.text}",
        )
        await mess.edit_media(file, reply_markup)


@dp.callback_query_handler(text="page_details_users")
async def get_whois_of_page(query: CallbackQuery):
    data = dict(await whois_table.get_whois_from_db(query.message.caption.split("\n\n")[-1]))
    await query.answer(
        text=(
            f"Ip: {data['ip']}\n\n"
            f"Country: {data['country']}\n"
            f"City: {data['city']}\n\n"
            f"Organization: {data['organization']}"
        ),
        show_alert=True,
    )

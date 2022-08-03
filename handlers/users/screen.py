import asyncwhois
import validators
import whois
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

from core.loader import dp
from utils.screenshot_page import Screener
from utils.whois import upload_whois_to_db


@dp.message_handler(content_types=ContentType.TEXT)
async def handle_link_message(msg: types.Message):
    if not validators.url(msg.text):
        await msg.reply("Please, send correct url", parse_mode=ParseMode.MARKDOWN)
    else:
        mess = await msg.answer_photo(
            types.InputFile("./media/1x1.png"), "Your image is processing..."
        )
        await upload_whois_to_db(mess.message_id, msg.text)
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
    a = whois.whois(query.message.caption.split("\n\n")[-1])
    res1 = await asyncwhois.aio_whois_ipv4("64.233.191.255")
    result = await asyncwhois.aio_whois_domain("query.message.caption.split('\n\n')[-1]")
    message = f"IP: 2"
    await query.answer(text="Пошел нахуй", show_alert=True)

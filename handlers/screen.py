import time

from aiogram import types
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
    InputMedia,
)

from core.db.db_api import whois_table
from core.loader import dp
from utils.screenshot_page import Screener


async def handle_link_message(msg: types.Message):
    st = time.time()
    mess = await msg.answer_photo(types.InputFile("./media/1x1.png"), "Your image is processing...")
    reply_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Page WHOIS", callback_data="page_details_users")
    )
    file = InputMedia(
        media=InputFile(await Screener(msg.text, msg.from_id).screen_page()),
        caption=(
            f"Your screenshot!\n\n"
            f"{msg.text}\n\n"
            f"Time of processing: {round(time.time()-st)} seconds"
        ),
    )
    await mess.edit_media(file, reply_markup)


@dp.callback_query_handler(text="page_details_users")
async def get_whois_of_page(query: CallbackQuery):
    data = dict(await whois_table.get_whois_from_db(query.message.caption.split("\n\n")[1]))
    await query.answer(
        text=(
            f"Ip: {data['ip']}\n\n"
            f"Country: {data['country']}\n"
            f"City: {data['city']}\n\n"
            f"Organization: {data['organization']}"
        ),
        show_alert=True,
    )

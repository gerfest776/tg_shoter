import aiofiles
import validators
from aiogram import types
from aiogram.types import ParseMode
from aiogram.types.message import ContentType


from core.loader import dp, bot
from utils.screenshot_page import Screener


@dp.message_handler(content_types=ContentType.TEXT)
async def link_message(msg: types.Message):
    if not validators.url(msg.text):
        await msg.reply("Please, send correct url", parse_mode=ParseMode.MARKDOWN)
    else:
        # mess = await msg.answer_photo(types.InputFile("./media/1000-7.jpeg"), "Your image is processing...")
        await msg.answer_photo(types.InputFile(await Screener(msg.text).screen_page()))

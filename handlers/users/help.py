from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from core.loader import dp
from filters import IsPrivate
from handlers.users.buttons import reply_help_button


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = [
        "Just send me a link to get screenshot of your page!",
    ]
    await message.answer("\n".join(text), reply_markup=reply_help_button)

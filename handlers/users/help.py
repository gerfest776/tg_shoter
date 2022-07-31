from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from core.loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'I can take a screenshot of a web page.',
        'To do this, just send me a link',
    ]
    await message.answer('\n'.join(text))

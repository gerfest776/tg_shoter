import logging

from aiogram import Dispatcher

from core.config import settings


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(settings.ADMIN, "Bot is running...")

    except Exception as err:
        logging.exception(err)

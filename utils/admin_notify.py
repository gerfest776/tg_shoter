import logging

from aiogram import Dispatcher

from config import settings


async def on_startup_notify(dp: Dispatcher):
    for admin in settings.admins:
        try:
            await dp.bot.send_message(admin, "Bot is running...")

        except Exception as err:
            logging.exception(err)

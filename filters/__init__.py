from aiogram import Dispatcher
from loguru import logger

from .chat_filter import IsGroup, IsPrivate


def setup(dp: Dispatcher):
    logger.info("Connecting filters...")
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)

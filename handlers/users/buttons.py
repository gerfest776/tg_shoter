from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reply_help_button = ReplyKeyboardMarkup(resize_keyboard=True)
reply_help_button.add(KeyboardButton("/help"))

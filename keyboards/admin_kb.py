from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_admin = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Код верный', callback_data='right'))

kb_admin_free = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Верно', callback_data='free_cup_done'))
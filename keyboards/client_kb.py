from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_client = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Отметить купленную чашку', callback_data='cup')).add(
    InlineKeyboardButton(text='Получить бесплатный кофе', callback_data='get_free'))


b1 = KeyboardButton('Я в Биографии')
b2 = KeyboardButton('Новинки и акции(позднее)')

kb_client_entry = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_entry.add(b1).add(b2)

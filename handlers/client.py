from keyboards.client_kb import kb_client, kb_client_entry
from keyboards.admin_kb import kb_admin, kb_admin_free
from aiogram import Dispatcher
from aiogram import types
from create_bot import bot
from random import randint
from data_base import sqlite_db

ID = None


# Приветствие
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет 👋\nКаждая шестая чашка кофе бесплатно!',
                           reply_markup=kb_client_entry)


# Кнопка "Я в Биографии"
async def entry_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=kb_client)


# Проверка кода
async def get_cup(callback: types.CallbackQuery):
    await callback.message.edit_text('Сообщите бариста четырехзначный код', reply_markup=None)
    await coffee(message=callback.message)



# Запись в БД новой чашки
async def paste_info(callback: types.CallbackQuery):
    await put_data(message=callback.message)
    await callback.answer(f'{ID}+1 чашка', show_alert=True)


# Подтверждение бесплатной чашки
async def get_free(callback: types.CallbackQuery):
    await callback.message.edit_text('Ожидайте подтверждения от бариста', reply_markup=None)
    await get_free_cup_q(message=callback.message)


# Внесение изменений в БД (Удаление одной бесплатной чашки)
async def get_free_1(callback: types.CallbackQuery):
    await get_free_cup(message=callback.message)
    await callback.answer(f'{ID}Бесплатная чашка!', show_alert=True)


# Проверка кода
async def coffee(message: types.Message):
    code = randint(1000, 9999)
    await bot.send_message(message.chat.id, f"{code}")
    await bot.send_message("-1001649374253", f"Проверьте код: {code}", reply_markup=kb_admin)


# Запись в БД новой чашки
async def put_data(message: types.Message):
    sqlite_db.cur.execute(f"INSERT INTO cup(id, amount, free_cups) SELECT {ID}, 0, 0 WHERE NOT EXISTS(SELECT 1 FROM "
                          f"cup WHERE id = {ID})")
    sqlite_db.cur.execute(f"UPDATE cup SET amount = amount + 1 WHERE id = {ID}")
    sqlite_db.cur.execute(f"UPDATE cup SET free_cups = free_cups + 1, amount = 0 WHERE amount = 5")
    sqlite_db.base.commit()


# Подтверждение бесплатной чашки
async def get_free_cup_q(message: types.Message):
    amount_free_cups = sqlite_db.cur.execute(f'SELECT free_cups FROM cup WHERE id = {ID}').fetchone()
    sqlite_db.base.commit()
    await bot.send_message("-1001649374253", f"У гостя {amount_free_cups[0]} бесплатных чашек")
    await bot.send_message("-1001649374253", f"Подтвердить бесплатный кофе?", reply_markup=kb_admin_free)


# Внесение изменений в БД (Удаление одной бесплатной чашки)
async def get_free_cup(message: types.Message):
    sqlite_db.cur.execute(f"UPDATE cup SET free_cups = free_cups - 1 WHERE id = {ID}")
    sqlite_db.base.commit()
    # await bot.send_message("-1001649374253", f"Бесплатная чашка!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(entry_command, lambda message: 'Я в Биографии' in message.text)
    dp.register_callback_query_handler(get_cup, text='cup')
    dp.register_callback_query_handler(paste_info, text='right')
    dp.register_callback_query_handler(get_free, text='get_free')
    dp.register_callback_query_handler(get_free_1, text='free_cup_done')

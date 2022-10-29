from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

with open("TOKEN.txt", "r") as file:
    TOKEN = f'{file.readline()}'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

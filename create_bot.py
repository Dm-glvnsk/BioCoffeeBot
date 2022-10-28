from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5683777800:AAE8idnZFdn-CD6hMm0dckdFzJzowv8W8ZY'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

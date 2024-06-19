# 1. Importing  libraties 
import logging
import os 

from aiogram import Bot, Dispatcher
from aiogram.types import Message #catching for all updates from this type
from aiogram.filters.command import Command # for comands /start, /help and others

#2. Initialization of objects 
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


#3 comand start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'hei, {user_name}!'
    logging.info(f'{user_name} {user_id} kjører bot')
    await bot.send_message(chat_id=user_id, text=text)


#4 alle message
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name[0]} {user_id}: {text}')
    await message.answer(text=text)

#5startprotsesor
if __name__ == '__main__':
    dp.run_polling(bot)
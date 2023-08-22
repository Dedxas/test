from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pymysql
from config import host, user, password, db_name



TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer('Иди нахуй отсюда')
                               
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет! ты долбаеб?')
   else:
       await msg.answer('Ты долбаеб?')

if __name__ == '__main__':
   executor.start_polling(dp)					


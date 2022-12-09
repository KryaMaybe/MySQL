# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message
import pymysql
from config import dbHost, dbUser, dbPassword, dbName


#Connection to database from config.py file
connection = pymysql.connection(dbHost, dbUser, dbPassword, dbName)

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")

# Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	text = f'''Привет! {message.from_user.full_name}
Барев дзес, Ахпер Джан
Для работы бота в группе необходимо дать ему права администратора и включить все разрешения ;) .'''
await message.answer(text=text)
analytic(message.from_user.username, message.from_user.id, message.from_user.full_name, message.text)

def analytic(nickname, tgid, fullname, command):
	cursor = connection.cursor()
	cursor.execute("INSERT INTO users(user_nickname, user_tgid, user_fullname, user_command) VALUES ('%s', '%s', '%s', '%s')" % (nickname, tgid, fullname, command))
	connection.commit()
	cursor.close()

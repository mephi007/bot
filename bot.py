import telebot 
import time
from io import BytesIO

token = '694896074:AAFfXqgRXygr6ZUJ02mwIKfGeTlEKuxHg0A'
bot = telebot.TeleBot(token = token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing? send '/help' to know further action")

@bot.message_handler(commands = [ 'help'] )
def send_help(message):
	bot.reply_to(message , '''type the following for more interaction
							 '/image' to get image
							 '/status' to get status of 
							 	sensors ''')
# chat_id = bot.get_updates()[-1].message.chat.id
# bot.send_message(chat_id= chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

chat_id = bot.get_updates()[-1].message.chat.id
@bot.message_handler(commands=['image'])
def send_image(message):
	# bot.send_photo(chat_id= chat_id, photo= open('image.jpg', 'rb'))
	bio = BytesIO()
	bio.name = ' image.jpg'
	image.save(bio, 'JPG')
	bio.seek(0)
	bot.send_photo(chat_id, photo = bio)

# @bot.message_handler (commands = ['echo']):
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.polling()
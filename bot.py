import telebot 
import time
#from io import BytesIO

token = '694896074:AAFfXqgRXygr6ZUJ02mwIKfGeTlEKuxHg0A'
bot = telebot.TeleBot(token = token)
chat_id = bot.get_updates()[-1].message.chat.id
#bot.send_message(chat_id= chat_id, text="Welcome ")

@bot.message_handler(commands=['start'])
def send_welcome(message,str):
	str = "Howdy, how are you doing? send '/help' to know further action"
	bot.reply_to(message, str )

#bot = telebot.TeleBot(token = token)
@bot.message_handler(commands = [ 'help'] )
def send_help(message):
	bot.reply_to(message , '''type the following for more interaction
							 '/image' to get image
							 '/status' to get status of 
							  sensors ''')
# chat_id = bot.get_updates()[-1].message.chat.id
# 
#bot = telebot.TeleBot(token = token)
#chat_id = bot.get_updates()[-1].message.chat.id 
@bot.message_handler(commands=['image'])
def send_image(chat_id, photo):
	bot.send_photo(chat_id= chat_id, photo= open('image.jpg', 'rb'))
	
	# bio = BytesIO()
	# bio.name = ' image.jpg'
	# image.save(bio, 'JPG')
	# bio.seek(0)
	#bot.send_photo(chat_id=chat_id, photo = 'image.jpg')
##echo
# @bot.message_handler (commands = ['echo']):
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
##

@bot.message_handler(func=lambda message: message.text == "hi")
def handle_message(message):
	bot.reply_to(message, "hello wazzup")

@bot.message_handler(func=lambda message: message.text is not None)
def handle_text_doc(message):
	text = message.text
	# print(text)

	bot.reply_to(message , " khush ho jaa")

bot.polling()
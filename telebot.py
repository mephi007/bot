import telegram
import picamera 
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler
import RPi.GPIO as GPIO
from picamera import PiCamera





GPIO.setmode(GPIO.BCM)
trig = 4
echo = 17

GPIO.setup( trig, GPIO.OUT)
GPIO.setup(echo , GPIO.IN)


def sensor(trig , echo):
	GPIO.output(trig ,False)
    
	time.sleep(2)
	GPIO.output(trig,True)

	time.sleep(.00001)
	GPIO.output(trig,False)

	while GPIO.input(echo)==0:
		start=time.time()
	while GPIO.input(echo)==1:
		end=time.time()
	duration=end-start
	distance=duration*17150
	distance=round(distance,2)
	return distance	

def camera():
	camera = Picamera()
	camera.start_preview()
	sleep(0.1)
	camera.capture('/home/pi/Desktop/image.jpg')
	camera.stop_preview()


token = '694896074:AAFfXqgRXygr6ZUJ02mwIKfGeTlEKuxHg0A'
updater = Updater(token = token)
bot = telegram.Bot(token)
intro = { ' hey' : 'hello' , 
					'how are you' : ' I am fine, how are you? tell me how can i help you',
					'status' :  ' here is the data'
				}
           
dispatcher = updater.dispatcher      
   

updates = []
#
while not updates:
	updates=bot.getUpdates()
	
text = updates[-1].message.text
print(text)

chat_id = updates[-1].message.chat.id
print(chat_id)

def start(bot , update):
	bot.send_message(chat_id = chat_id , text="I'm a bot, send '/help' to get instruction")     
  
def help(bot , update):
	bot.send_message(chat_id = chat_id , text=" I am able to send to you an alert if obstacle is nearer than 10 cm Send '/status' to know the sensor value Send '/image' to get image	")
	
def status(bot , update):
	dist = sensor(trig , echo)
	if (dist < 10): 
		bot.send_message(chat_id = chat_id , text=" DANGER") 
		camera()
		bot.sendPhoto(chat_id = chat_id , tetx = 'image.jpg')
	else:
		bot.send_message(chat_id = chat_id , text=" all ok")
		
def image (bot , update):
	bot.send_message(chat_id = chat_id , text=" ") 
#	time.sleep(5)

start_handler = CommandHandler('start' , start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help' , help)
dispatcher.add_handler(help_handler)
	
status_handler = CommandHandler('status' , status)
dispatcher.add_handler(status_handler)
	
image_handler = CommandHandler('image' , image)
dispatcher.add_handler(image_handler)
	

	

updater.start_polling()
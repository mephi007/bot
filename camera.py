from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(1)
camera.capture('/home/pi/Desktop/bot/bot/image.jpg')
camera.stop_preview()


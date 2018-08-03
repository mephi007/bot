import RPi.GPIO as pi
from time 

trig = 4
echo = 17

pi.setmode(pi.BCM)
pi.setup(trig , pi.OUT)
pi.setup(echo , pi.IN)

while True:

	pi.output(trig, False)
	time.sleep(2)

	pi.output(trig, True)
	time.sleep(0.000001)
	pi.output(trig , False)

	pi.output(trig, True)

	start = time.time()
	end = time.time()

	while (pi.input(echo) == 0):
		start = time.time()

	while (pi.input(echo) == 0):
		end = time.time()

	duration = end - start

	distance = (duration * 34300) / 2

	print("----------------------------------------------------------")
	print(distance)

	time.sleep(2)
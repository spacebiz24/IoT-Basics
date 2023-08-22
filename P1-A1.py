import RPi.GPIO as GP
import time as T

pins = [13, 19, 26]
GP.setmode(GP.BCM)

for pin in pins:
	GP.setup(pin, GP.OUT)

try:
	while True:
		for i in range(8):
			for j in range(3):
				GP.output(pins[j], i & (1 << j) != 0)
			T.sleep(1)
except KeyBoardInterrupt:
	GP.cleanup()
	exit()

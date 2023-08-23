import RPi.GPIO as GPIO
import time

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM) # GPIO.BOARD -> pin no.

# GPIO Setup
LED = [18,23,17,4] # in Reverse order
GPIO.setup(LED, GPIO.OUT)

counter = 0

# Main
try:
  while True:
	  for LEDIndex in range(len(LED)):
		  GPIO.output(LED[LEDIndex], counter&(1<<LEDIndex) != 0)
	counter += 1
except KeyBoardInterrupt:
  GPIO.cleanup()
  exit()

# Blink an LED at periodic intervals by interfacing with RPi 4

import RPi.GPIO as GPIO
import time

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM) # GPIO.BOARD -> pin no.

# GPIO Setup
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Main
try:
  while True:
    GPIO.output(LED_PIN, True)
    time.sleep(1)
    GPIO.output(LED_PIN, False)
    time.sleep(1)
except KeyBoardInterrupt:
  GPIO.cleanup()
  exit()

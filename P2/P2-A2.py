# Switch multiple LEDs with a delay based on LDR readings

import RPi.GPIO as GPIO
import time

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)

# GPIO Setup
LDR_PIN = 22
GPIO.setup(LDR_PIN, GPIO.IN)
LED = [18,21]
GPIO.setup(LED, GPIO.OUT)

# Main
while True:
    if GPIO.input(LDR_PIN):
      GPIO.output(LED[0], 1)
      time.sleep(1)
      GPIO.output(LED[1], 1)
    else:
      GPIO.output(LED[0], 0)
      time.sleep(0.5)
      GPIO.output(LED[1], 0)

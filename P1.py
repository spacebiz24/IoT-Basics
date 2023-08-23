import RPi.GPIO as GPIO
import time

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM) #GPIO.BOARD -> pin no.

# GPIO Setup
GPIO.setup(LED_PIN, GPIO.OUT)
LED_PIN = 18

# Main
try:
  while True:
    GPIO.output(LED_PIN, True)
    time.sleep(1)
    GPIO.output(LED_PIN, False)
    time.sleep(1)
except KeyBoardInterrupt:
  GP.cleanup()
  exit()

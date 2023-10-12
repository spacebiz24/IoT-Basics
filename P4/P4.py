# Interface Motor Relay with RPi to control its operation

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RELAY_PIN = 22

GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(RELAY_PIN, True)
        time.sleep(4)
        GPIO.output(RELAY_PIN, False)
        time.sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

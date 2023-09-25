# Control the direction of motor spin

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin Setup
RELAY_PINS = [22, 27]
GPIO.setup(RELAY_PINS, GPIO.OUT)

try:
    while True:
        GPIO.output(RELAY_PINS, True)
        time.sleep(4)
        GPIO.output(RELAY_PINS, False)
        time.sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin Setup
RELAY_PIN_1 = 22
RELAY_PIN_2 = 27
GPIO.setup(RELAY_PIN_1, GPIO.OUT)
GPIO.setup(RELAY_PIN_2, GPIO.OUT)

try:
    while True:
        GPIO.output(RELAY_PIN_1, True)
        GPIO.output(RELAY_PIN_2, True)
        time.sleep(4)
        GPIO.output(RELAY_PIN_1, False)
        GPIO.output(RELAY_PIN_2, False)
        time.sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

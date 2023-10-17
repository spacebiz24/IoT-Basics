# Interfacing soil moisture sensor with RPi and control the motor

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RELAY_PIN = 22
SOIL_PIN = 24

GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(SOIL_PIN, GPIO.IN)

try:
    while True:
            GPIO.output(RELAY_PIN, GPIO.input(SOIL_PIN))
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

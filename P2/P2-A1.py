# Switch multiple LEDs based on LDR readings

import RPi.GPIO as GPIO

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
    GPIO.output(LED, GPIO.input(LDR_PIN))

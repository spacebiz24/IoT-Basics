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
    LDR_Value = GPIO.input(LDR_PIN)
    Delay = 1 if LDR_Value else 0.5
    GPIO.output(LED[0], LDR_Value)
    time.sleep(Delay)
    GPIO.output(LED[1], LDR_Value)

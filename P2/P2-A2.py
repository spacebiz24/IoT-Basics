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
    for LEDIndex in range(len(LED)):
        LDR_Value = GPIO.input(LDR_PIN)
        GPIO.output(LED[LEDIndex], LDR_Value)
        time.sleep(1 if LDR_Value else 0.5)

# Interface an LDR to the RPi to turn ON an LED in the presence of light

import RPi.GPIO as GPIO

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)

# GPIO Setup
LDR_PIN = 22
GPIO.setup(LDR_PIN, GPIO.IN)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Main
while True:
    GPIO.output(LED_PIN, GPIO.input(LDR_PIN))

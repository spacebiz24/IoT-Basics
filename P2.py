import RPi.GPIO as GPIO

# Pi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM) # GPIO.BOARD -> pin no.

# GPIO Setup
LDR_PIN = 22
GPIO.setup(LDR_PIN, GPIO.IN)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Main
while True:
    if GPIO.input(LDR_PIN):
      GPIO.output(LED_PIN, 1)
    else:
      GPIO.output(LED_PIN, 0)

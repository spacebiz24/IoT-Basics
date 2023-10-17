import RPi.GPIO as GPIO
import time

GPIO.setwarnings(0)
GPIO.setmode(BCM)

LDR_PIN = 22
GPIO.setup(LDR_PIN,GPIO.IN)
LED_PIN = [18,21]
GPIO.setup(LED,GPIO.OUT)

while True:
  LDR_Value = GPIO.input(LDR_PIN)
  Delay = 1 if LDR_Value else 0.5
  #switch between LEDs at different speeds based on LDR_Value
  GPIO.output(LED[0],1)
  time.sleep(Delay)
  GPIO.output(LED[0],0)

  GPIO.output(LED[1],1)
  time.sleep(Delay)
  GPIO.output(LED[1],0)

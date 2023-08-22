import RPi.GPIO as GP
import time as T

LED_PIN = 18

GP.setmode(GP.BCM)
GP.setup(LED_PIN, GP.OUT)
try:
  while True:
    GP.output(LED_PIN, True)
    T.sleep(2)
    GP.output(LED_PIN, False)
    T.sleep(2)
except KeyBoardInterrupt:
  GP.cleanup()
  exit()

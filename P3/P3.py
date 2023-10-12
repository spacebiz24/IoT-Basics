# Interface DHT11 sensor with RPi to display temperature and humidity readings

import board
import adafruit_dht
import time
import psutil

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Sensor Setup
DHT11Pin = board.D21 # GPIO 21
DHT11Sensor = adafruit_dht.DHT11(DHT11Pin)

while True:
  try:
    temperatureCelsius = DHT11Sensor.temperature
    humidityPercent = DHT11Sensor.humidity

    print(f"Temperature: {temperatureCelsius} C, Humidity: {humidityPercent} %")
    time.sleep(1)

  except RuntimeError:
    time.sleep(1)
    continue
  except KeyboardInterrupt:
    DHT11Sensor.exit()

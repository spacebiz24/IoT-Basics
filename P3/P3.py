import board
import adafruit_dht
import time

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

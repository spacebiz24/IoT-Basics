import board
import adafruit_dht
import time

# Sensor Setup
dht_pin = board.D21 # GPIO 21
dht_sensor = adafruit_dht.DHT11(dht_pin)

while True:
  try:
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity

    print(f"Temperature: {temperature} C, Humidity: {humidity} %")
    time.sleep(1)

  except RuntimeError:
    time.sleep(1)
    continue
  except KeyboardInterrupt:
    dht_sensor.exit()

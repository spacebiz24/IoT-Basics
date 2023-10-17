# Interface Sensor data to Thingspeak through RPi

import http.client
import urllib
import time
import board
import adafruit_dht
import psutil

for proc in psutil.process_iter():
    if proc.name() in ['libgpiod_pulsei', 'libgpiod_pulsein']:
        proc.kill()

DHT11Pin = board.D4
sensor = adafruit_dht.DHT11(DHT11Pin)

key = "6HA8IJ1FEHXSR9A3" # Write API Key

def readTemperature():
    while True:
        try:
            temperatureCelsisus = sensor.temperature
            humidityPercent = sensor.humidity
        except:
            continue
        
        params = urllib.parse.urlencode({'field1':temperatureCelsisus,'field2':humidityPercent,'key':key})
        headers = {"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print("Temperarture:{}*C Humidity:{}%".format(temperatureCelsius, humidityPercent))
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("Connection Failed")

if __name__ == "__main__":
    while True:
        readTemperature()

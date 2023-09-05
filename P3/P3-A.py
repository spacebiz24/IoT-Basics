# Interface Sensor data to Thingspeak through RPi

import http.client
import urllib
import time
import board
import adafruit_dht
import psutil

key = "6HA8IJ1FEHXSR9A3"

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

DHT11Pin = board.D4
sensor = adafruit_dht.DHT11(DHT11Pin)

def readTemperature():
    while True:
        try:
            temperatureCelsisus = sensor.temperature
            humidityPercent = sensor.humidity
        except:
            continue
        
        params = urllib.parse.urlencode({'field1':temp,'field2':humidity,'key':key})
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

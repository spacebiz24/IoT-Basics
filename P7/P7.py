import time
import datetime
import csv
import MySQLdb
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()

IR_SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

Database = MySQLdb.connect(host = "localhost", user = "exampleuser", passwd = "pimylifeup", db = "exampledb")
Cursor = Database.cursor()

while True:
    temperatureCelsius = GPIO.input(IR_SENSOR_PIN)
    currentTime = datetime.datetime.utcnow()
    print(temperatureCelsius)
    Cursor.execute('''INSERT INTO SensorStats(Date_Time, IRSensorStat) VALUES(%s, %s);''', (currentTime, temperatureCelsius))
    Database.commit()
    time.sleep(1)

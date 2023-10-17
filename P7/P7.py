import time
from pytz import timezone
from datetime import datetime
import csv
import MySQLdb
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

IR_SENSOR_PIN = 4
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

Database = MySQLdb.connect(host = "localhost", user = "exampleuser", passwd = "pimylifeup", db = "exampledb")
Cursor = Database.cursor()

while True:
    Proximity = GPIO.input(IR_SENSOR_PIN)
    currentTime = datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S.%f")
    print(Proximity)
    Cursor.execute('''INSERT INTO SensorStats(Time, Proximity) VALUES(%s, %s);''', (currentTime, Proximity))
    Database.commit()
    time.sleep(1)

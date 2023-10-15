import bluetooth
import RPi.GPIO as GPIO

# RPi Setup
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)

# Pin Setup
ledPin = 18
GPIO.setup(ledPin, GPIO.OUT)

Host = ""
Port = 1
Server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Bluetooth Socket Created")

try:
    Server.bind((Host, Port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")

Server.listen(1)

Client, Address = Server.accept()
print("Connected To: ", Address)
print("Client: ", Client)

try:
    while True:
        Data = int(Client.recv(1024))
        print(Data)
        if Data:
            GPIO.output(ledPin, True)
            Message = "Light ON"
            print("ON")
        elif !Data:
            GPIO.output(ledPin, False)
            Message = "Light OFF"
            print("OFF")
        else:
            Message = "Type 1 or 0"
        Client.send(Message)
        
except:
    GPIO.cleanup()
    Client.close()
    Server.close()

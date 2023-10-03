import bluetooth
import RPi.GPIO as GP

led = 4
GP.setmode(GP.BCM)
GP.setup(led, GP.OUT)
host = ""
port = 1
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

print("Bluetooth Socket Created")

try:
    server.bind((host, port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")

server.listen(1)

client, address = server.accept()
print("Connected To", address)
print("Client:", client)

try:
    while True:
        data = client.recv(1024)
        data = int(data)
        print(data)
        if data == 1:
            GP.output(led, True)
            send = "Light ON"
            print("ON")
        elif data == 0:
            GP.output(led, False)
            send = "Light OFF"
            print("OFF")
        else:
            send = "Type 1 or 0"
        client.send(send)
        
except:
    GP.cleanup()
    client.close()
    server.close()
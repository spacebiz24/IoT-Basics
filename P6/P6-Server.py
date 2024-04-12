import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

messageFromServer = "Hello UDP Client"
BytesToSend = str.encode(messageFromServer)
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
ServerSocket.bind((localIP, localPort))
print("UDP Server Up and Running")

while True:
    message, address = ServerSocket.recvfrom(bufferSize)
    print(f"Message From Client: {message}")
    print(f"Client IP Address: {address}")
    ServerSocket.sendto(BytesToSend, address)

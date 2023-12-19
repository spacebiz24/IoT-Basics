import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

messageFromClient = "Hello UDP Server"
BytesToSend = str.encode(messageFromClient)
ClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
ClientSocket.sendto(BytesToSend, (localIP, localPort))

serverMessage = ClientSocket.recvfrom(bufferSize)
print(f"Message From Server: {serverMessage[0]}")

import socket

localIP = "127.0.0.1"
localPort = 20001
messageFromClient = "Hello UDP Server"
bufferSize = 1024

serverAddressPort = (localIP, localPort)
BytesToSend = str.encode(messageFromClient)
ClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
ClientSocket.sendto(BytesToSend, serverAddressPort)

serverMessage = ClientSocket.recvfrom(bufferSize)
messageReceived = "Message From Server: {}".format(serverMessage[0])
print(messageReceived)

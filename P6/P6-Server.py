import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

messageFromServer = "Hello UDP Client"
bytesSend = str.encode(messageFromServer)
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
ServerSocket.bind((localIP, localPort))
print("UDP Server Up and Running")

while True:
    bytesAddress = ServerSocket.recvfrom(bufferSize)
    message = bytesAddress[0]
    address = bytesAddress[1]
    clientMessage = "Message From Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)
    print(clientMessage)
    print(clientIP)
    ServerSocket.sendto(bytesSend, address)

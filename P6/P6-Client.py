import socket
localIP = "127.0.0.1"
localPort = 20001
messageFromClient = "Hello UDP Server"
bufferSize = 1024

serverAddressPort = (localIP, localPort)
bytesSend = str.encode(messageFromClient)
ClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
ClientSocket.sendto(bytesSend, serverAddressPort)

serverMessage = ClientSocket.recvfrom(bufferSize)
message = "Message From Server: {}".format(serverMessage[0])
print(message)
import socket

localIP = "127.0.0.1"
localPort = 20001
buffersize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)

# Bind to address and IP
UDPServerSocket.bind((localIP,localPort))

print("UDP server up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientmsg = "message from client: {}".format(message)
    clientIP = "client IP address: {}".format(address)

    print(clientmsg)
    print(clientIP)

    # sending reply to client
    UDPServerSocket.sendto(bytesToSend,address)
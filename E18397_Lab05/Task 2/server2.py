import socket

localIP = "127.0.0.1"
localPort = 20000
buffersize = 1024
msgFromServer = "Hello UDP Client(from server 2)"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)

# Bind to address and IP
UDPServerSocket.bind((localIP,localPort))

print("UDP server 2 up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientmsg = "message from client: "+ message.decode()
    clientIP = "client IP address: {}".format(address)

    print(clientmsg)
    print(clientIP)

    # sending reply to client
    UDPServerSocket.sendto(bytesToSend, address)


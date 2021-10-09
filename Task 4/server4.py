import socket

localIP = "127.0.0.1"
localPort = 20001
buffersize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET,type = socket.SOCK_DGRAM)

# changing the boffer size
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 200000)

# Bind to address and IP
UDPServerSocket.bind((localIP,localPort))

print("UDP server up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientmsg = "Number from client: {}".format(message.decode())

    print(clientmsg)

    # sending reply to client
    UDPServerSocket.sendto(message, address)
    
import socket

serverAddressPort = ("127.0.0.1",20001)
buffersize = 1024

# create UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

# getting number from user
msgFromClient = input("Enter a Number: ")
bytesToSend = str.encode(msgFromClient)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend,serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(buffersize)
msg = "Message from server: "+msgFromServer[0].decode()

print(msg)


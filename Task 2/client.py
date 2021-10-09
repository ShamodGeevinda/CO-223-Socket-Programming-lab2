import socket

msgFromClient = "Helllo UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1",20001)
serverAddressPort2 = ("127.0.0.1",20000)
buffersize = 1024

# create UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend,serverAddressPort)
UDPClientSocket.sendto(bytesToSend,serverAddressPort2)

# receiving and printing the messahge from 1 st server
msgFromServer = UDPClientSocket.recvfrom(buffersize)
msg1 = "Message from server 1: "+msgFromServer[0].decode()
print(msg1)

# receiving and printing the messagee from 2 nd server
msgFromServer = UDPClientSocket.recvfrom(buffersize)
msg2 = "Message from server 2: "+msgFromServer[0].decode()
print(msg2)


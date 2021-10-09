import socket

serverAddressPort = ("127.0.0.1",20001)
buffersize = 1024

# create UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

# getting number from user
n =int(input("Enter a Number: "))

# loop to send numbers to the server
for i in range(0,n):
    bytesToSend = str.encode(str(i+1))

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend,serverAddressPort)

# loop to recceive messages from the server
while (True):
    msgFromServer = UDPClientSocket.recvfrom(buffersize)
    msg = "Number from server: "+msgFromServer[0].decode()

    print(msg)


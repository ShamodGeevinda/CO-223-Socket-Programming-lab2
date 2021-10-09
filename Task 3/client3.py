import socket

msgFromClient = "Helllo UDP Server"
bytesToSend = str.encode(msgFromClient)
buffersize = 1024

# create UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPClientSocket.connect(("127.0.0.1",20001))
# Send to server using created UDP socket

UDPClientSocket.send(bytesToSend)

msgFromServer = UDPClientSocket.recv(buffersize).decode()
msg = "Message from server: "+msgFromServer

print(msg)
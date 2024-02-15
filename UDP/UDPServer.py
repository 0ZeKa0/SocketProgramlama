
from socket import *
serverPort = 1883
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server is ready to recieve")
while True:
 mesaj, clientAdres = serverSocket.recvfrom(2048)
 modifiedMessage = mesaj.decode().upper()
 serverSocket.sendto(modifiedMessage.encode(), clientAdres)
 
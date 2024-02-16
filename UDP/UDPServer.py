
from socket import *
sunucuPort = 1883
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', sunucuPort))
print("Server is ready to recieve")
while True:
 mesaj, aliciAdres = serverSocket.recvfrom(2048)
 degisenMesaj = mesaj.decode().upper()
 serverSocket.sendto(degisenMesaj.encode(), aliciAdres)

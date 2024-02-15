from socket import *

""" client kodunun içinde server bilgilerine yer verilmelidir. """

serverisim = '192.168.1.5'
serverport = 1883

clientSocket= socket(AF_INET, SOCK_DGRAM)
mesaj = input('girdi: ')
clientSocket.sendto(mesaj.encode(), (serverisim,serverport))
degisenMesaj, serverAdres = clientSocket.recvfrom(2048)
print(degisenMesaj.decode())
clientSocket.close()

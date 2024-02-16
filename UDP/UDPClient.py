from socket import *

""" client kodunun içinde server bilgilerine yer verilmelidir. """

sunucuismi = ''
sunucuport = 1883

clientSocket= socket(AF_INET, SOCK_DGRAM)
mesaj = input('girdi: ')
clientSocket.sendto(mesaj.encode(), (sunucuismi,sunucuport))
degisenMesaj, sunucuAdres = clientSocket.recvfrom(2048)
print(degisenMesaj.decode())
clientSocket.close()

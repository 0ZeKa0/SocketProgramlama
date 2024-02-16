from socket import *
sunucuismi = ''
sunucuPort = 1883
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((sunucuismi, sunucuPort))
kelime = input('Girdi:')
clientSocket.send(kelime.encode())
degisenKelime = clientSocket.recv(1024)
print('From Server:', degisenKelime.decode())
clientSocket.close()
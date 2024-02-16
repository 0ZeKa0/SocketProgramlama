from socket import *
serverismi = '192.168.1.5'
serverPort = 1883
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverismi, serverPort))
kelime = input('Girdi:')
clientSocket.send(kelime.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
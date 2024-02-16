from socket import *
sunucuPort = 1883
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', sunucuPort))
serverSocket.listen(1)
print('The server is ready to reciev')
while True:
 connectionSocket, addr = serverSocket.accept()
 kelime = connectionSocket.recv(1024).decode()
 buyutulmusKelime = kelime.upper()
 connectionSocket.send(buyutulmusKelime.encode())
 connectionSocket.close()
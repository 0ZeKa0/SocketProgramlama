from socket import *
serverPort = 1883
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to reciev')
while True:
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024).decode()
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence.encode())
 connectionSocket.close()
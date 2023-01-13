import socket
import threading

LOCALHOST = ""
PORT = 3451

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALHOST, PORT))
print("Сервер запущен!")


class ClientThread(threading.Thread):

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Новое подключение: ", clientAddress)

    def run(self):
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == 'exit':
                print("Отключение")
                self.csocket.send(bytes("Вы успешно отключены от сервера", "UTF-8"))
                break
            else:
                self.csocket.send(bytes(msg, "UTF-8"))


while True:
    server.listen(1)
    clientsock, clientaddress = server.accept()
    nexthreed = ClientThread(clientaddress, clientsock)
    nexthreed.start()


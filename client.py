import socket
from threading import Thread

SERVER = ""
PORT = 3451

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def task():
    while True:
        in_data = client.recv(4096)
        print("От сервера: ", in_data.decode())


def task2():
    while True:
        out_data = input()
        client.sendall(bytes(out_data, 'UTF=8'))
        print("Отправлено: " + str(out_data))


t1 = Thread(target=task2)
t2 = Thread(target=task)

t1.start()
t2.start()
t1.join(timeout=60)
t2.join(timeout=60)
print("END")

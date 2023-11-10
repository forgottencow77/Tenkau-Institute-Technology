import socket

sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv.connect(("raspberrypi", 27015))

while True:
    data = sv.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

sv.close()
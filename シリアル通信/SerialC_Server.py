# ソケット通信モジュール
import socket
import time
from threading import Timer

# IPv4形式のソケット通信を行うオブジェクトを作成 v6は別
sv = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

## IPアドレスとポートをバインドしてソケットを受け付ける
# 引数は(IPアドレス, ポート番号)のタプル
sv.bind(('', 27015))
#受付開始
sv.listen(5)
print('Server Running')

def backgroundcontroller():
    message = 'Hello Client'
    print(message)
    clientsocket.send(bytes(message, "utf-8"))
    Timer(5, backgroundcontroller).start()

while True:
    clientsocket, address = sv.accept()
    print(f"Conncetion from {address} has been established")
    backgroundcontroller()

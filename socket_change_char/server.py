import socket

# socketの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET:IPv4, SOCK_STREAM:TCP通信
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # {adress} has been established 回避
s.bind((socket.gethostname(), 12345)) # IPとportの設定
s.listen() # 並列処理リクエスト

clientsocket, adress = s.accept() # 接続の受信を行う
print("adress is", adress)
print("Connection from {adress} has been established!")
while True:
    recvline = clientsocket.recv(1024).decode() # clientからのデータ受取
    # 文字ごとの処理
    result_str = ""
    for mozi in recvline:
        if mozi.islower():
            result_str += mozi.upper()
        elif mozi.isupper():
            result_str += mozi.lower()
        else:
            result_str += mozi
    # serverにデータを送信
    clientsocket.send(result_str.encode("utf-8"))
    # "Q"が受信されたら終了
    if result_str == "q":
        break
# 接続の切断
clientsocket.close()

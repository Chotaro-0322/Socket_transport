import socket

# socketの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET:IPv4, SOCK_STREAM:TCP通信
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # {adress} has been established 回避
s.bind((socket.gethostname(), 12345)) # IPとportの設定
s.listen() # 並列処理リクエスト
flag = False # 終了フラグ

clientsocket, adress = s.accept() # 接続の受信を行う
print("adress is", adress)
print("Connection from {adress} has been established!")
recvline = clientsocket.recv(1024).decode() # clientからのデータ受取
# ファイルの中身を読み込む処理
try:
    with open(recvline, "r") as f:
        result_str = f.read()
except FileNotFoundError:
    print("ファイルが存在しませんでした")
    result_str = "null" # ファイルが存在しなかったら"null"を返す.
# serverにデータを送信
clientsocket.send(result_str.encode("utf-8"))
# 接続の切断
clientsocket.close()

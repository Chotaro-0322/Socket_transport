import socket

# socketの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET:IPv4, SOCK_STREAM:TCP通信
s.connect((socket.gethostname(), 12345)) # serverと同じIPアドレスとportに接続
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # {adress} has been established 回避
while True:
    keyinput = input(">>>") # キーボードからの入力受け取り
    s.send(keyinput.encode()) # データをserverに送信
    msg = s.recv(1024) # serverからのデータの返信を受け取る
    full_msg = b''
    if len(msg) <= 0: 
        break
    if msg.decode("utf-8") == "q": # "Q"が入力されたら終了
        print("終了します")
        break
    else:
        print("結果は", msg.decode("utf-8")) # 結果を表示













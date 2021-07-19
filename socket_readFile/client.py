import socket

# socketの作成
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET:IPv4, SOCK_STREAM:TCP通信
s.connect((socket.gethostname(), 12345)) # serverと同じIPアドレスとportに接続
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # {adress} has been established 回避
flag = False # 初期フラグの設定
while True:
    keyinput = input("ファイル名を入力してください >> ") # キーボードからの入力受け取り
    s.send(keyinput.encode()) # データをserverに送信
    msg = s.recv(1024).decode("utf-8") # serverからのデータの返信を受け取る
    if len(msg) <= 0: 
        break

    if not msg == "null": # ファイルが存在していた場合
        print("ファイルの中身は", msg) # 結果を表示
        print("ファイル名:", keyinput[:-4] + "_copy.txt に保存します.")
        with open(keyinput[:-4] + "_copy.txt", "w") as f:
            f.write(msg)
            break
    else: # 存在しなかった場合は, もう一度ファイル名を入力するように要求
        print("ファイル名が間違っている可能性があります. もう一度入力してください")

 
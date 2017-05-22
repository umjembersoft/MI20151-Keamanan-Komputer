import socket
host = "192.168.0.1"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn, addr = s.accept()
print addr, "Selamat Anda Sudah Terhubung dengan Serverku.py"
conn.send("Terima Kasih karena telah berkomunikasi dengan Serverku.py")
conn.close()
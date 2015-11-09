import socket

host ="0.0.0.0"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
conn, addr = s.accept()
print addr, "Selamat anda sudah terhubung dengan Serverku.py"
conn.send("Terima kasih karena anda telah berkomunikasi dengan Serverku.py")
conn.close()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 12345
s.connect((host,port))
print s.recv(1024)
s.send("Hai Serverku.py, Clientku.py ingin berkomunikasi")
s.close()

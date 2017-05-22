import socket

host = "0.0.0.0"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
while True:
	conn, addr = s.accept()
	print addr, "NOW Connected"
	conn.send("Thank you for connecting")
	conn.close()

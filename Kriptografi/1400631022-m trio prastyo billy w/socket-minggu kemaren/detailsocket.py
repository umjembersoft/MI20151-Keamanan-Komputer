import socket

def get_protnumber(prefix):
	return dict ((getattr(socket, a),a)
				for a in dir (socket)
				if a.startswith(prefix))

proto_fam = get_protnumber ('AF_')
type = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')
for res in socket.getaddrinfo('www.unmuhjember.ac.id','http'):
	family, socktype, proto, canonname, sockaddr = res
	
	print 'Family :', proto_fam[family]
	print 'Type : ' , type[socktype]
	print 'Protocol :' , protocols[proto]
	print 'Canincal name:' , canonname
	print 'Socket addres:' , sockaddr 

import socket

ip = '127.0.0.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))

s.listen(5)

while true:
	conn, addr = s.accept()
	conn.send('Welcome to the first server tcp\n')
	print ("connection from %s:%d" %(addr[0],addr[1])
	conn.send('#######')
	msg = conn.recv(1024)
	print 'message received: %s' %msg
	conn.close()
	break
s.close()

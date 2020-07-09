import socket

ip = '1.1.1.1'
port = 8888

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip, port)

while True:
	msg = input('##')
	udp.sendto(msg,dest)
	msg,conn = udp.recvfrom(1024)
	print (msg)
udp.close()

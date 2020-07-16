import socket
import sys

host = sys.argv[1]
host = sys.argv[2] if len(sys.argv) >= 3 else ''

msg = 'GET /%s HTTP/1.1\nHost: %s\n\n' % (path,host)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)

print ('connecting')
s.connect((socket.gethostbyname(host,80))

print('sending')
s.send('msg')

print ('receiving')
data = ''
while 1:
	try:
		buf = s.recv(1024)
		data += buf
	except:
		s.close()
	print data
import socket
from time import sleep

host = '127.0.0.1'
port = 5000
ips = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print('server started')

quitS = False
while not quitS:
	data, addr = s.recvfrom(1024)
	if 'quitS' in str(data):
		print('server will close in...')
		for i in reversed(range(4)):
			sleep(1)
			print (i)
		quitS = True
		break
	print (str(addr) + ': '+str(data))
	if addr not in ips:
		ips.append(addr)
	for ip in ips:
		s.sendto(data, ip)

s.close()

import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# this might be database or a file
di = {'17BIT0382': 'gizem', '17BEC0647': 'ezgi', '17BEC0150': 'osman',
	  '17BCE2119': 'ömer', '17BIT0123': 'enes'}

while True:
	# receiving name from client
	name, addr1 = UDPServerSocket.recvfrom(bufferSize)

	# receiving pwd from client
	pwd, addr1 = UDPServerSocket.recvfrom(bufferSize)

	name = name.decode()
	pwd = pwd.decode()
	msg = ''

	if name not in di:
		msg = 'name does not exist'
		flag = 0
	else:
		flag = 1
		if di[name] == pwd:
			msg = "pwd match"
		else:
			msg = "pwd wrong"

	bytesToSend = str.encode(msg)
	# sending encoded status of name and pwd
	UDPServerSocket.sendto(bytesToSend, addr1)






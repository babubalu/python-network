import socket
Host= ''
port = 8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,port))
while True:
	message = raw_input("Your message:  ")
	s.send(message)
	print ("awaiting reply")
	reply=s.recv(1024)
	print "received: ",repr(reply)
s.close()

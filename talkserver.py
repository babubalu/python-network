import socket
Host=''	#Babu: try localhost or your actual IP
	#Try to get your IP dynamically using APIs

port=8000 
	#Babu: 0-1023 ports importance
	#know the important of fixed ports and user-defined ports
	#Learn the well known ports like 80, 22, 23 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,port))
s.listen(2)

	#Babu:Try experimenting with backlog parameter
 	#learn when backlog will be useful
conn,addr=s.accept()
print 'connected by', addr
while True:

	data=conn.recv(1024)
	print 'received:',repr(data)
	reply=raw_input("Reply: ")
	conn.sendall(reply)
conn.close


#modifying to make it as a multichat client

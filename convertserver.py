import socket
for host in ['www.python.org','www.google.com','www.facebook.com']:
    try:
	print host,socket.gethostbyname(host)
    except socket.error,msg:
	print "Error"

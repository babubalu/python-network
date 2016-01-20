import socket
for host in ['www.google.com','www.facebook.com']:
    print host
    try:
	#hostname=socket.gethostbyname_ex(host)
        hostname,aliases,addresses=socket.gethostbyname_ex(host)
	print 'Hostname:',hostname,'Aliases: ',aliases,'Address :',addresses

    except socket.error,msg:
	print "Error",host,msg
    

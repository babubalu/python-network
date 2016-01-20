import socket
hostname,aliases,addresses=socket.gethostbyaddr('31.13.78.35')
print 'Hostname: ',hostname
print 'aliases:',aliases
print 'addresses: ',addresses

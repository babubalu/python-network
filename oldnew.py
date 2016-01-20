import socket
import urlparse
for port in [80,25,995,21,70,143]:
    print urlparse.urlunparse(
         (socket.getservbyport(port),'example.com','/','','','')
         )

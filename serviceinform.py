import socket
from urlparse import urlparse
for url in['smtp://mail.example.com']:
    parsed_url=urlparse(url)
    port=socket.getservbyname(parsed_url.scheme)
    print parsed_url.scheme,port

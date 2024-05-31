
# A python library to parse web data to terminals.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## Initializes a request 
mysock.connect(('data.pr4e.org',80)) # connects to the request
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # Gets the metadata from the HTTP host and encodes it too.
mysock.send(cmd) # Finally sends it

while True:
    data = mysock.recv(512) # recives 512 characters only
    if (len(data) < 1): # if less than 1 just break it.
        break
    print(data.decode()) # decodes the data
mysock.close() # closes it

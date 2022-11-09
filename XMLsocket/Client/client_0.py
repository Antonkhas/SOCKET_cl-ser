import socket
import config_client

socket = socket.socket()
socket.connect(("localhost", 55210))

file = open(config_client.PATH_TO_FILE, "rb")
stream = file.read(55536)

while stream:
    socket.send(stream)
    stream = file.read(55536)
socket.close()

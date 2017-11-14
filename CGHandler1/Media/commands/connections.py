import socket


HOSTS = {
    'LOCALHOST' : '127.0.0.1',
}
PORTS = {
    'AMCP' : 5250,
    'OSC' : 7250,
}


# def CreateAMCPConnection(host,port):
#     sock = socket.create_connection((host, port))
#     return sock

def SendAMCPCommand(host, port, cmd):
    sock = socket.create_connection((host, port))
    sock.send(cmd)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

# def AbortAMCPConnection(sock):
#     sock.shutdown(socket.SHUT_RDWR)
#     sock.close()
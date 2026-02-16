import socket

def ipgrab():
    sn = socket.gethostname()
    si = socket.gethostbyname(sn)
    return print(sn,"\n",si)

ipgrab()
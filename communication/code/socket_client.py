import socket
import time

addr = ('127.0.0.1', 6666) # same as server

s = socket.socket()
s.connect(addr) # raise exception for a bad connection


try:
    msg_get = s.recv(4096)
    print(msg_get.decode('ascii'))
    for i in range(5):
        msg = b'glgjssyqyhfbqz'
        s.send(msg)
        print('Message to %s:%s : %s' % (*addr, msg.decode('ascii')))
        time.sleep(1)
finally:
    s.close()
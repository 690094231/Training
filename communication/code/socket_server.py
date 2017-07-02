import socket
import threading

def socket_link(sock, addr):
    print('Accept connection from %s:%s' % addr)
    try:
        sock.send(b'houa!') # send data by ascii code.
        while True:
            msg = sock.recv(4096) # receibe message of 4096 bytes.
            if(len(msg) > 0):
                print('Message from %s:%s : %s' % (*addr, msg.decode('ascii')))
            else: # disconnect if not received.
                break
    finally:
        sock.close() # close socket to release port occupation.

if __name__ == '__main__':
    # set protocol ipv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind 127.0.0.1(loopback address),port 6666
    s.bind(('127.0.0.1', 6666))

    # listen
    backlog = 1 # max connections
    s.listen(backlog)
    print('Waiting for connection.')

    # accept a new connection
    sock, addr = s.accept()

    # create a thread to handle connections.
    t = threading.Thread(target=socket_link, args=(sock, addr))
    t.start()
    print('nmbyztxyngdxw')
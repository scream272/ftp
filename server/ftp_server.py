

# !/usr/bin/env python
# _*_coding:utf-8_*_

'''
import socket
import os

server = socket.socket()
server.bind(('localhost', 9998))

server.listen(5)

while True:
    conn, addr = server.accept()
    print 'new connection:', addr

    while True:
        print 'wait for new command.'
        data = conn.recv(1024)
        print data
        if not data:
            print 'client connection is broken.'
            break

    print 'receive new command:"%s" ' % data

    cmd = data[:3].lower()
    args = data[3:]

# cmd, args = data.split()

    if os.path.isfile(args):
        f = open(args, 'wb')
#        file_size = os.stat(args).st_size
#        conn.send(str(file_size))

        buf = conn.recv(1024)
        f.write(buf)
        f.close()


server.close()

'''



'''
import socket
import os
import hashlib

server = socket.socket()
server.bind(("localhost", 9999))

server.listen(5)

while True:
    conn, addr = server.accept()
    print("new conn:", addr)

    while True:
        print("wait new command")
        data = conn.recv(1024)
        if not data:
            print("client connection is broken")
            break
        cmd, filename = data.split()
        if os.path.isfile(filename):
            f = open(filename, "rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size))
            conn.recv(1024)
            for line in f:
                conn.send(line)
                m.update(line)
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest())

        print(cmd, filename)

server.close()
'''

































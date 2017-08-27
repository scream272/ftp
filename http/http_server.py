# !/usr/bin/env python
# _*_coding:utf-8_*_

# 通过代理服务器进行HTTP访问，这样就省去了对URL进行DNS解析的步骤
# 当数据正确返回时，为了将实际数据从协议中分离出来保存，需要对HTTP数据包进行解析得到Content-Length,然后在

import socket
import re

HOST = ''
PORT = 8000

index_content = '''
HTTP/1.1 200 ok
Content-Type:text/html
'''
file = open('index.html', 'r')
index_content += file.read()
file.close()

reg_content = '''
HTTP/1.1 200 ok
Content-Type:text/html
'''
file = open('reg.html', 'r')
reg_content += file.read()
file.close()

file = open('T-mac.jpeg', 'rb')
pic_content = '''
HTTP/1.x 200 ok
Content-Type: image/jpeg
'''
pic_content += file.read()
file.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

while True:
    conn, addr = sock.accept()
    request = conn.recv(1024)

    method = request.split(' ')[0]
    src = request.split(' ')[1]

    print 'connect by: ', addr
    print 'Request is:\n', request

    if method == 'GET':
        if src == '/index.html':
            content = index_content
        elif src == '/T-mac.jpeg':
            content = pic_content
        elif src == '/reg.html':
            content = reg_content
        elif re.match('^/\?.*$', src):
            entry = src.split('?')[1]  # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            content += entry
            content += '<br /><font color="green" size="7">register successs!</p>'
        else:
            continue

    #deal with POST method
    elif method == 'POST':
        form = request.split('\r\n')
        entry = form[-1]      # main content of the request
        content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
        content += entry
        content += '<br /><font color="green" size="7">register successs!</p>'


    else:
        continue

    conn.sendall(content)

    # close connection
    conn.close()



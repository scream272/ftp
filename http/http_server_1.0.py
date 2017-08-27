# !/usr/bin/env python
# _*_coding:utf-8_*_

import socket, os, threading, sys, signal, stat
import time, struct, re, traceback
import pprint
from collections import defaultdict

host = 'localhost'
port = 8080
timeout = 15
DOCUMENT_ROOT = os.getcwd() + '/'

HTTP_PROTOCOL = 'HTTP/1.1'

cgiexts = ['cgi', 'php', 'sh', 'py']

mimes = {"application/ogg":      " ogg",
         "application/pdf":      " pdf",
         "application/xml":      " xsl xml",
         "application/xml-dtd":  " dtd",
         "application/xslt+xml": " xslt",
         "application/zip":      " zip",
         "audio/mpeg":           " mp2 mp3 mpga",
         "image/gif":            " gif",
         "image/jpeg":           " jpeg jpe jpg",
         "image/png":            " png",
         "text/css":             " css",
         "text/html":            " html htm",
         "text/javascript":      " js",
         "text/plain":           " txt asc",
         "video/mpeg":           " mpeg mpe mpg",
         "video/quicktime":      " qt mov",
         "video/x-msvideo":      " avi",}

#
mm = {}
for t in mimes.keys():
    for ext in mimes[t].split():
        mm[ext] = t
mimes = mm

default_set = set([
    'index.html'
    'index.php'
])

def handle_php(conn):
    handle_cgi(conn)

handlers = {}

class Request(object):
    def __init__(self, header):
        self.request = ''
        self.uri = ''
        self.orig_uri = ''
        self.http_method = ''
        self.http_version = ''
        self.request_line = ''
        self.headers = defaultdict(list)
        self.content_length = -1
        self.body = ''
        self.query_string = ''

        self._parse(header)

    def _parse(self, header):
        lines = header.splitlines()
        self.request_line = lines[0]
        method, uri, protocol = self.request_line.split()

        self.orig_uri = self.uri = uri
        qpos = uri.find('?')
        if qpos != -1:
            self.query_string = uri[qpos + 1:]
            self.uri = uri[:qpos]


        self.http_method = method
        self.http_version = protocol

        for i in range(1, len(lines)):
            key, value = lines[i].split(': ')
            self.headers[key].append(value)

        self.content_length = self.headers.get('Content-Length', [-1])[0]



class Response(object):
    RESPONSE_FROM_FILE = 0
    RESPONSE_FROM_MEM = 1

    def __init__(self):
        self.content_length = -1
        self.keepalive = False
        self.headers = defaultdict(list)
        self.response_type = Response.RESPONSE_FROM_MEM
        self.response = ''
        self.response_fd = -1



class Connection(object):
    def __init__(self, sockfd, remote_ip):
        self.sockfd = sockfd
        self.remote_ip = remote_ip
        self.keepalive = False

        self.reset()


    def reset(self):
        self.state = None
        self.keepalive = False
        self.http_status = -1
        self.request = None
        self.respone = None
        self.environment = {}



class ThreadRun(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    def run(self):
        handle_connection(self.conn)
        self.conn.sockfd.close()
        print '[', self.getName(), ']', 'ended'


class MultiThreadServer(object):
    def __init__(self, host, port):
        self.listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listenfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listenfd.bind((host, port))
        self.listenfd.listen(5)

    def server_forver(self):
        while True:
            clientfd, clientaddr = self.listenfd.accept()

            # timeout for 5 seconds
            clientfd.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, struct.pack('11', timeout, 0))

            # select, fork or multithread
            conn = Connection(clientfd, clientaddr[0])

            th = ThreadRun(conn)
            th.start()

def get_header(buf):
    ' return header and end '

















































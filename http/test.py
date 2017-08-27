# !/usr/bin/env python
# _*_coding:utf-8_*_

import socket, os, threading, sys, signal, stat
import time, struct, re, traceback
import pprint
from collections import defaultdict

'''
需要解决的问题点：1.Python中的struct模块
               2.setsockopt设置socket状态
               3.Python多线程
               4.正则表达式
               5.HTTP协议原理
               6.cgi编程
'''


# 在网络中传输诸如int,char之类的基本数据结构时，需要能有一种机制将某些特定的结构体类型打包成二进制流的字符串，然后再网络传输，而接受端也应该能
# 通过某种机制进行解包还原出原始的结构http://www.cnblogs.com/coser/archive/2011/12/17/2291160.html

# http://www.cnblogs.com/hateislove214/archive/2010/11/05/1869886.html

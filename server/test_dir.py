# !/usr/bin/python
# _*_coding:utf-8_*_


'''
import re


line = 'Cats are smarter than dogs'

matchObj = re.match('(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print 'matchObj.group(): ', matchObj.group()
    print 'matchObj.group(1): ', matchObj.group(1)
    print 'matchObj.group(2): ', matchObj.group(2)
else:
    print 'No match!'

'''

# ???????????????????????????????

import thread
import time
'''
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s %s" % (threadName, time.ctime(time.time()))

try:
    thread.start_new_thread(print_time, ("Thread-1", 2), )
    thread.start_new_thread(print_time, ("Thread-2", 4), )

except:
    print "ERROR: unable to start thread"

while True:
    pass
'''

'''
import threading
import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting" + self.name
        print

'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# ???????
db = MySQLdb.connect("localhost","root","root","TESTDB" )

# ??cursor()????????
cursor = db.cursor()

# ??execute????SQL??
cursor.execute("SELECT VERSION()")

# ?? fetchone() ??????????
data = cursor.fetchone()

print "Database version : %s " % data

# ???????
db.close()


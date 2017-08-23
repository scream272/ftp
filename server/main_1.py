#!/usr/bin/python
# -*- coding: utf-8-*-


'''
Python实现FTP客户端传输文件：
1.工具：ftplib库
2.需要实现的功能：

    下载和上传文件
    下载和上传文件/目录
    异常处理
3.To do list:连接指定服务器，上传文件（输入指定文件名，上传到指定服务器端指定文件夹下）

'''
import os
from ftplib import FTP
import time
import tarfile  # tarfile模块的主要作用是用于加压和解压文件

'''
    input:需要连接的 ftp server,登陆用户名和密码（用nickname和帐号分开整个usrname属性比较好）
    output:连接成功的句柄   
'''
def ftpconnect(host,username,password):
    ftp = FTP()  # 设置变量
    ftp.connect(host, 21, 500)
    ftp.login(username, password)

    print ftp.getwelcome()
    return ftp


'''
    input:要上传的文件名（本地文件）：如果不存在该文件或路径，就创建一个新文件
          指定的服务器
          服务器端指定文件夹
    FTP.storbinary(cmd,文件名, 文件对象 [,块大小])     # 上传FTP文件
'''


def uploadfile(ftp_server, remotefile, localfile):
    bufsize = 1024
    #ftp_server.storbinary('STOR' + os.path.basename(remotefile), open(localfile, 'rb'), bufsize)
    ftp_server.storbinary('STOR %s' % remotefile, open(localfile, 'rb'), bufsize)
    ftp_server.close()



def downloadfile(ftp_server,remotefile,localfile):
    bufsize = 1024
    ftp_server.retrbinary('RETR %s' % remotefile, open(localfile, 'wb').write, bufsize)
    ftp_server.close()

if __name__ == '__main__':
    ftp_server = ftpconnect('127.0.0.1', 'ahriy', 'root') #127.0.0.1
    downloadfile(ftp_server, '/home/ahriy/ftp/First', './Hello')
   # uploadfile(ftp_server, '/home/ahriy/ftp/First', './Hello')

    ftp_server.close()
    # ftp_server.quit()理论上也可以实现，但是会报错





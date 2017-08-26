#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 显示文件 "a2.py" 信息
statinfo = os.stat('test.py')

print statinfo.st_size
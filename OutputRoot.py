#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

f_out = open('MyFiles.txt', 'w')

for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    f_out.write(root + '\r\n')

    """
    for name in dirs:
        #打印目录绝对路径
        f_out.write(os.path.join(root, name) + '\r\n')
    """
f_out.close()

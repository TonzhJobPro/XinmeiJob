#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, codecs, os

def u2g(string):
	return string.decode('gbk').encode('gbk')
dirpath = os.getcwd()
print dirpath
os.listdir(dirpath)
print os.listdir(dirpath)
f_out = codecs.open('filelist.txt', 'w', 'utf-8')
for root, dirs, files in os.walk(dirpath, topdown=False):
	for name in files:
		print(os.path.join(root, name)) #打印文件绝对路径
		#f_out.write(os.path.join(root, name).decode('gbk') + '\r\n')
	for name in dirs:
		print(os.path.join(root, name)) #打印目录绝对路径
		f_out.write(os.path.join(root, name).decode('gbk')+ '\r\n')
f_out.close()

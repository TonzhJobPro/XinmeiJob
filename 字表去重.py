#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
用途：字表1按照字表2顺序排序
前提：需要处理的txt文件，放在该python脚本同目录下
使用方法：
	1.命令行下：字表重排序.py 字表1.txt 字表2.txt
	2.程序自动识别输入txt是编码还是字形，执行完之后会生成'字表1_新排序.txt'
"""

import sys, codecs, os



input_file_name = sys.argv[1]
f_only = codecs.open(input_file_name.replace('.txt', '') + '_only' + '.txt', 'w', 'utf-8')
onlylist = set()


if not os.path.exists(os.path.join('.', input_file_name)):
	print '请输入正确txt文件名，该文件必须和本脚本在同目录下'
	sys.exit()
	
f_in = open(input_file_name, 'r')
input_list = []
is_unicode = False

text = f_in.read()
for encoding_way in ['ascii','gbk','utf-8','utf-16','utf-16-le', 'utf-16-be']:
	try:
		text = text.decode(encoding_way)
		break
	except UnicodeDecodeError:
		continue
	except:
		print '无法读取输入文件，请检查！'
		sys.exit()	
lines = text.splitlines()
for line in lines:
	str = ''
	line = line.replace('\r', '')
	line = line.replace('\n', '')
	line = line.replace(' ', '')
	line = line.strip()
	for char in line:
		if char not in onlylist:
			onlylist.add(char)
			str += str(char)
		if len(str) > 0:
			f_only.write(str)
f_in.close()


f_only.close()


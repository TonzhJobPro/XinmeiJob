#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
用途：根据编码文件，提取图片库中指定字图片
前提：需要处理的txt编码文件，图片库，放在该python脚本同目录下
使用方法：
	1.准备字符编码txt文件，要求要提取的字以Unicode编码形式，可用“rename_char_to_unic.py”进行转码
	
	2.命令行下：该脚本全名加空格加需要提取的txt编码文件全名
	2.程序自动识别输入txt是编码，执行完之后会在图片库目录下生成"MyPNG"文件夹，保存提取的图片
"""

import os, fnmatch
from shutil import copy
import sys

def __find_all_files(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result
png_file_list = __find_all_files('*.png', '.')
dest_dir = os.path.dirname(png_file_list[0]) + '\\MyPNG'
if not os.path.isdir(dest_dir):
    os.makedirs(dest_dir)
for png_file_item in png_file_list:
	a = os.path.basename(png_file_item)
	b = hex(ord(a.replace('.png','')))+'.png'
	os.rename(a, b)
print 'a'
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys, fnmatch, random, math

stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('gbk')
sys.stdout = stdout


def __find_all_files(pattern, path):
	result = set()
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.add(os.path.join(root, name))
	return result

#read config
obj = sys.argv[1]
obj_file_list = __find_all_files('*.'+obj, '.')
for obj_file_item in obj_file_list:
	print obj_file_item
	
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-13 18:34:06
# @Author  : guang liang (guang.liang@xinmei365.com)
# @Link    : http://www.xinmei365.com
# @Version : 0.1

import os
import struct
import logging
logging.basicConfig(	# 设置logging级别和格式
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

class ttfstream(object):

	def __init__(self, fd, mode):
		if not isinstance(fd, file):
			with open(fd, mode) as f:
				self.stream = f.read()
		else:
			f = fd

		self.offset = 0
		self.ttf = {
			'header' : {'type':'>IHHHH', 'size':12, 'sfntVersion':0, 'numTables':1, 'searchRange': 2, 'entrySelector': 3, 'rangeShift':4  },
			'entry'  : {'type':'>4sLLL', 'size':16, 'tag':0, 'checkSum':1, 'offset':2, 'length': 3 },
		}
		self.offsetdir = {}
		
		# Table Directory
		self.header = self.getrecord('header')
		logging.debug("offset table: {}".format(self.header))
		
		table_num = self.header[ self.ttf['header']['numTables'] ]
		for i in range(table_num):
			r = self.getrecord('entry')		# referenced in form of [ttf['entry']['tag']]
			self.offsetdir[r[self.ttf['entry']['tag']]] = r

	def getrecord(self, key, table_pos=0):
		offset = self.offset
		size = self.ttf[key]['size']
		if table_pos != 0:
			offset = table_pos
		offset += size
		self.offset = offset
		logging.debug('getrecord: %d %d'%(offset, size))
		return struct.unpack(self.ttf[key]['type'], self.stream[offset - size: offset])

	def getstring(self, size, off):
		offset = self.offset
		off += offset
		self.offset = offset
		return struct.unpack(">%ds"%(size), self.stream[off: off+size])[0]

	@classmethod
	def calc_tbl_chksum(data, table_pos, length):
		chksum = 0
		end = table_pos + ((length+3) & ~3)
		while table_pos < end:
			try:
				chksum += struct.unpack('>L', data[table_pos:table_pos+4])[0]
			except struct.error, e:
				print 'In calc_tbl_chksum: ', e
				s =  ba.hexlify( data[table_pos:table_pos+4] )
				print 'data[%d:%d] = %s'%(table_pos, table_pos+4, s) , 'len=', len(data[table_pos:table_pos+4]), 'len(data)=', len(data)
				value = int( s, 16)
				chksum += value

			table_pos += 4
		return chksum & 0xFFFFFFFF # type ULONG is 32-bit


def find_table(fd, table_tag):
	font = ttfstream(fd, 'r')
	return table_tag in font.offsetdir


if __name__ == '__main__':

	filename = '../_svn/Flora-color/Flora-color.ttf'
	if find_table(filename, 'CBDT'):
		print 'Ture'
	else:
		print 'False'

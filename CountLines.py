#!/usr/bin/env python

import os

work_dir = './'
file_filter = '.py;.c;.cpp;.h'
count = 0
file_list = []

if __name__ == '__main__':
    ext_filter = file_filter.strip('.').split(';')
    for root,dirs,files in os.walk(work_dir):
        for filename in files:
            try:
                if filename.split('.')[1] in ext_filter:
                    file_list.append(filename)
                    with open(os.path.join(root,filename), 'rU') as f:
                        lines = f.readlines()
                        count = count + len(lines) - lines.count('\n')
            except IndexError:
                #print filename
                pass
                    
    #print file_list
    print count
    raw_input("Press Any key to exit ... ")
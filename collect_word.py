#！ usr/bin/env python
import re
import sys
import os
import time

f_path = 'd:/Python/zfc.txt'		# define file aeecss path
print('Get a string from the file')
time.sleep(5)
f = open(f_path)
s1 = f.read()
f.close()

p = re.compile(r'\w+')
m = p.findall(s1)
print(m)
m_list = set(m)
print(m_list)
for item in m_list:
	print('The', item, 'has found', m.count(item))
#！usr/bin/python

import re
import sys
import time
import os

f_path = 'd:/Python/zfc.txt'		# define file aeecss path
print('Get a string from the file')
time.sleep(5)
f = open(f_path)
s1 = f.read()
print('the original string:', s1)
f.close()
s2 = s1[::-1]
print('the reverted string:', s2)
s_len = len(s1)
if s_len in [0, 1]:
	print('the string is invalid.')
if s1 == s2:
	print('This string is a palindome.')
else:
	print('This string is not a palindome.')
	
# s_len = len(s1)
# if s_len in [0, 1]:
	# print('the string is invalid, script stop')
	# os.exit()
# l_compare = s_len // 2		# get compare times
# x = 0
# while x < l_compare:
	# m1 = re.match(r'[s1[x]. s1[(l_compare - 1)]
	# if m1:
		# print('This string is a palindrome')   
	# else:
		# print('This string is not a palindrome')
# else:
	
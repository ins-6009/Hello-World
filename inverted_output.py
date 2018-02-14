#！usr/bin/env python

import sys

in_str = input('please input a string:\n')
print('###################################')
print('The original string:', in_str)
print('###################################')
print('The inverted order string:', in_str[::-1])

# count = len(in_str) - 1
# count
# while count >= 0:
	# print(in_str[count], end="")	# next print will follow previous print, not in new line
	# count -= 1
# print('\nThe string has been converted')
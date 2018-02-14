#！usr/bin/python
import sys
import re

s = input('Please input a string:\n')
p = re.compile(r'[aeiouAEIOU]')		# list all vowel characters
m = p.findall(s)					# feedback a list of all match vowel character
print(m)
vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count_l = 0
for x in vowel_list:
	print(vowel_list[count_l], 'count:', m.count(x))
	count_l +=1

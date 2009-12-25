
import re


# helper-func: subinstr
# 
# @list of regex,sub -pairs
# @the string 
# {{{ subinstr()
def subinstr(list,newstr):
		for i in list:
				p = re.compile(i[0])
				newstr = p.sub(i[1], newstr)

		return newstr


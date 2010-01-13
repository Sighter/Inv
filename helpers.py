
import re
from settings import *
from output import *


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
# }}}

# readcid() Read the current id from current-file {{{
def readcid():
		fkt = "helpers.readcid"
		
		if os.path.isfile(fil_cur) == False:
				mprint(fkt,1,"Current Invoice id doesnt exists. Exiting")
				sys.exit(5)

		f = open(fil_cur, "r")
		id = f.readline().strip("\n")
		f.close()	

		if len(id) == 0:
				mprint(fkt,1,"No invoice marked as current. Exiting")
				sys.exit(5)

		return id

# }}}

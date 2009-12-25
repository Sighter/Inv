
# Function which create a texfile and a pdf,
# with the current invoice-data
import os, sys
from settings import *
from output import mprint
from helpers import subinstr

def create():
		fkt = "create.create"
		if os.path.isfile(fil_cur) == False:
				mprint(fkt,1,"Current Invoice id doesnt exists. Exiting")
				sys.exit(5)
		f = open(fil_cur, "r")
		id = f.readline()
		f.close()	

		if len(id) == 0:
				mprint(fkt,1,"No invoice marked as current. Exiting")
				sys.exit(5)
				
		# read the invoice-data from object-files
		fol_obj = os.path.join(fol_invobjects,id)

		objdata = invdata

		for i in objdata:
				f = open(os.path.join(fol_obj,i[0]), "r")
				i[1] = f.readline()
				f.close()


		# read the blueprint tex-file
		try:
			texfile = open(fil_pattern, "r")
		except:
			mprint(fkt,1,"No blueprint exists. Exiting")
			sys.exit()
		
		texfilestr = texfile.read()

		# create the substitute - list
		for i in objdata:
				i[0] = r"\$" + i[0]

		# substitute !
		texfilestr = subinstr(objdata,texfilestr)

		print(texfilestr)

		# create output tex-file
		f = open(os.path.join(fol_obj,"src.tex"), "w")
		f.write(texfilestr)
		f.close
		
		mprint(fkt,1,"Texfile written.")

		


		
				

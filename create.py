
# Function which create a texfile and a pdf,
# with the current invoice-data
import os, sys, subprocess
from settings import *
from output import mprint
from helpers import *

def writepdf(path):
		print(path)
		command = "pdflatex -etex -output-directory={} -interaction=nonstopmode {}".format(".",path)
		p = subprocess.Popen(command, shell = True)
		p.wait()

def create():
		fkt = "create.create"
		if os.path.isfile(fil_cur) == False:
				mprint(fkt,1,"Current Invoice id doesnt exists. Exiting")
				sys.exit(5)

		# Read the current id from current-file
		id = readcid()

		# read the blueprint tex-file
		try:
			texfile = open(fil_pattern, "r")
		except:
			mprint(fkt,1,"No blueprint exists. Exiting")
			sys.exit()
		
		texfilestr = texfile.read()

		# read the invoice-data from object-files
		fol_obj = os.path.join(fol_invobjects,id)

		objdata = invdata

		for i in objdata:
				f = open(os.path.join(fol_obj,i[0]), "r")
				i[1] = f.readline()
				f.close()

		# create the substitute - list
		for i in objdata:
				i[0] = r"\$" + i[0]

		# substitute !
		texfilestr = subinstr(objdata,texfilestr)

		# create output tex-file
		fil_texsrc = os.path.join(fol_obj,"src.tex")
		f = open(fil_texsrc, "w")
		f.write(texfilestr)
		f.close
		
		mprint(fkt,1,"Texfile written.")

		# creating the pdf in the root-folder
		writepdf(fil_texsrc)

		


		
				

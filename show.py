
# Function shows the invoice data
# of the invoice marked as current
# or specified -- todo
import os, sys, getopt
from settings import *
from output import mprint
from helpers import *

		

def show(args):
		fkt = "show.show"

		# parse arguments
		try:
			opts, args = getopt.getopt(args, "hd", ["help"])
		except getopt.GetoptError as err:
			print(err) # will print something like "option -a not recognized"
			sys.exit(2)
		
		if len(args) != 0:
				printall = False
		else:
				printall = True

		# Read the current id from current-file
		id = readcid()

				
		# read the invoice-data from object-files
		fol_obj = os.path.join(fol_invobjects,id)

		objdata = invdata

		for i in objdata:
				f = open(os.path.join(fol_obj,i[0]), "r")
				i[1] = f.readline()
				f.close()

		# print out the data
		if printall == True:
			print()
			for i in objdata:
					print(i[2]+":\n  "+i[1]+"\n")

		for i in args:
				for k in objdata:
						if i == k[0]:
								print(k[2]+":\n  "+k[1]+"\n")





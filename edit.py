
# Function shows the invoice data
# of the invoice marked as current
# or specified -- todo
import os, sys, getopt
from settings import *
from output import mprint
from helpers import *

		

def edit(args):
		fkt = "edit.edit"

		# parse arguments
		try:
			opts, args = getopt.getopt(args, "hd", ["help"])
		except getopt.GetoptError as err:
			print(err) # will print something like "option -a not recognized"
			sys.exit(2)

		promtall = False	
		if len(args) == 0:
				promtall = True
		
		# Read the current id from current-file
		id = readcid()
				
		# read the invoice-data from object-files
		fol_obj = os.path.join(fol_invobjects,id)

		objdata = invdata

		for i in objdata:
				f = open(os.path.join(fol_obj,i[0]), "r")
				i[1] = f.readline()
				f.close()

		# edit the data
		if promtall == False:
			count = 0
			for i in args:
					for k in objdata:
							if i == k[0]:
									try:
											k[1] = args[count+1]
									except:
											mprint(fkt,1,"Wrong arguments given")
					count = count +1
		
		# Promt through all the data
		else:
			for i in objdata:
				print(i[2]+":\n  "+i[1])
				k = input(" >")
				if len(k) != 0:
						i[1] = k

		# write the data back	
		for i in objdata:
				f = open(os.path.join(fol_obj,i[0]), "w")
				f.write(i[1])
				f.close()


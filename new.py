

# The function to create an ivoice-object


# Todo: Test if id exits

import os, sys, getopt
from output import mprint
from settings import *




def new(args):
	fkt = "new.new"
	
	# parse options
	try:
		opts, args = getopt.getopt(args, "hd", ["help"])
	except getopt.GetoptError as err:
		print(err) # will print something like "option -a not recognized"
		sys.exit(2)

	for o,a in opts:
			if o == "-d":
					writedefaults = True
			else:
					print("Undefined Arg or Option: "+ o)
					sys.exit(2)

	if len(args) != 1:
			mprint(fkt,1,"Exactly one argument required. bye ...")
			sys.exit(4)
	else:
			i_id = args[0]
	
	# check whether a folder with the given id exists
	if os.path.exists(os.path.join(fol_invobjects,i_id)) == True:
			mprint(fkt,1,"Invoice Id exists. Exiting ...")
			sys.exit(4)

	# check whether a .inv folder exits:
	if os.path.exists(fol) == False:
			mprint(fkt,1,"No Repo exits. bye ...")
			sys.exit(4)
	else:
			mprint(fkt,1,"Creating a new Invobject ...")

	# Create the Object-folder
	fol_instanz = os.path.join(fol_invobjects,i_id)
	os.mkdir(fol_instanz)
	
	# Create invoice data files
	for i in invdata:
		os.mknod(os.path.join(fol_instanz,i[0]))
	
	# feed the files with the hardcoded defaults
	if writedefaults == True:
		for i in invdata:
			f = open(os.path.join(fol_instanz,i[0]), "w")
			f.write(str(i[1]))
			f.close

	# Set the current id
	f = open(fil_cur, "w")
	f.write(i_id)
	f.close()

	# make a initial log entry
	# todo






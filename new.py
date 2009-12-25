

# The function to create an ivoice-object


# Todo: Test if id exits

import os, sys, getopt
from output import mprint
import settings


fol = ".inv"
fol_invobjects 	= os.path.join(fol,"invobjects")
fil_list		= os.path.join(fol,"listfile")
fil_log			= os.path.join(fol,"log")
fil_cur			= os.path.join(fol,"current")


def new(args):
	print(len(args))
	fkt = "new.new"
	
	# parse options
	try:
		opts, args = getopt.getopt(args, "h", ["help"])
	except getopt.GetoptError as err:
		print(err) # will print something like "option -a not recognized"
		sys.exit(2)
	print(len(args))
	if len(args) != 1:
			mprint(fkt,1,"Exactly one argument required. bye ...")
			sys.exit(4)
	else:
			i_id = args[0]
	
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
	for i in settings.invdata:
		os.mknod(os.path.join(fol_instanz,i[0]))


	# make a initial log entry
	# todo






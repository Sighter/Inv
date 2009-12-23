
# The function to init a repo

import os, sys
from output import mprint


cwd = os.getcwd()
fol = ".inv"
fol_invobjects 	= os.path.join(fol,"invobjects")
fil_list		= os.path.join(fol,"listfile")
fil_log			= os.path.join(fol,"log")

def init():
	fkt = "init.init"

	# check whether a .inv folder exits:
	if os.path.exists(fol) == True:
			mprint(fkt,1,"You have forgotten that here is already a repo. bye ...")
			sys.exit(3)
	else:
			mprint(fkt,1,"Creating a new repo ...")

	# Create all folders and files, or the "tree"
	mprint(fkt,1,"Creating folders and files")
	os.mkdir(fol)
	os.mkdir(fol_invobjects)
	os.mknod(fil_list)
	os.mknod(fil_log)

	# make a initial log entry
	# todo






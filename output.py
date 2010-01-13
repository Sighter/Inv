

def printhelp(fname):
		# Help for main
		if fname == "main":
				print("\n This is the Help vor \"inv\":\n")
				print(" Actions:")
				print("    init 	: Create an empty invoice repository")
				print("    new  	: Create an empty invoice Object")
				print("    create  	: Create a latex source file")
				print("    help  	: Print this help")
				print()



def mprint(target,level,msg):
		print("  --> " + target + ": "+msg)

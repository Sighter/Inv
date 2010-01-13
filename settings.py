
# Module for all settings

import os

# Invoice data-table

#  ID				Content						Long Name
invdata = [
[ "date",		r"21.01.1642",				r"Date"],
[ "service",	r"Klärgrubenreinigung",		r"Service"],
[ "hours",		r"",						r"Hours"],
[ "euph",		100,						r"Euro per hour"],
[ "id",			r"",						r"Invoice ID"],
[ "total",		100,						r"Total"],
[ "recn",		r"Don Joe",					r"Recipient - Name"],
[ "recst",		r"The Street 70",			r"Recipient - Street"],
[ "reczipc",	r"09642 Stadt",				r"Recipient - Zip Code and City"],
[ "sendern",	r"Klärmüller",				r"Sender - Name"],
[ "senderst",	r"Am Abfluss 20",			r"Sender - Street"],
[ "senderzipc",	r"02121 Grubental",			r"Sender - Zip Code and City"],
[ "vatn",		r"xxx/xxx/xxx/xxx",			r"VAT-Number"],
[ "accn",		r"xxxxxxxx",				r"Account Number"],
[ "blz",		r"blzxxxxx",				r"Bank Identification Code"],
[ "inst",		r"Bank Institut",			r"Bank Institute"],
[ "hp",			r"www.doe.to",				r"Homepage"],
[ "email",		r"doe@xxx.com",				r"E-Mail"],
]


fol = ".inv"
fol_invobjects 	= os.path.join(fol,"invobjects")
fil_list		= os.path.join(fol,"listfile")
fil_log			= os.path.join(fol,"log")
fil_cur			= os.path.join(fol,"current")
fil_pattern		= os.path.join(fol,"pattern.tex")
fil_patternh	= os.path.join(fol,"pattern_hours.tex")

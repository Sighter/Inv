
# Module for all settings

import os

invdata = [
[ "date",r"21.01.1642"],
[ "service",r"Klärgrubenreinigung"],
[ "hours",r""],
[ "euph",100],
[ "id",r""],
[ "total",100],
[ "recn",r"Don Joe"],
[ "recst",r"The Street 70"],
[ "reczipc",r"09642 Stadt"],
[ "sendern",r"Klärmüller"],
[ "senderst",r"Am Abfluss 20"],
[ "senderzipc",r"02121 Grubental"],
[ "vatn",r"xxx/xxx/xxx/xxx"],
[ "accn",r"xxxxxxxx"],
[ "blz",r"blzxxxxx"],
[ "inst",r"Bank Institut"],
[ "hp",r"www.doe.to"],
[ "email",r"doe@xxx.com"],
]


fol = ".inv"
fol_invobjects 	= os.path.join(fol,"invobjects")
fil_list		= os.path.join(fol,"listfile")
fil_log			= os.path.join(fol,"log")
fil_cur			= os.path.join(fol,"current")
fil_pattern		= os.path.join(fol,"pattern.tex")
fil_patternh	= os.path.join(fol,"pattern_hours.tex")

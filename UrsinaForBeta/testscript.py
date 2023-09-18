from GnuChanGE import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton



app = Ursina()



DropdownMenu('File', buttons=( DropdownMenuButton('New'), DropdownMenuButton('Open'), 
DropdownMenu('Reopen Project', buttons=(DropdownMenuButton('Project 1'), DropdownMenuButton('Project 2'))),
DropdownMenuButton('Save'), DropdownMenu('Options', buttons=(DropdownMenuButton('Option a'), DropdownMenuButton('Option b'))),
DropdownMenuButton('Exit')))

app.run()
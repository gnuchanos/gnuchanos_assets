from GnuChanGE import *
from mainmenu import MainMenu
from scenes import *



gc = GnuChanGE()

def changeScene():
    scene.clear()
    studio()

mainMenu = MainMenu(startGame=changeScene)




gc.runLoop()
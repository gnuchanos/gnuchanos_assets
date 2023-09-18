from GnuChanGE import *



class MainMenu(Entity):
    def __init__(self, startGame=None, options=None, exit=application.quit ,add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        colors = GColors()


        self.bg0 = GnuChanGE().gPanel(bg=colors.gnuchanColor, scaleX=.35, scaleY=1, y=0)
        self.bg1 = GnuChanGE().gPanel(bg=colors.gnuchanColor3, scaleX=.3, scaleY=.5, y=.15)

        self.start = GnuChanGE().gButton(text="Start Game", scaleX=.25, scaleY=.10, textScale=.1,
                             tcolor=colors.purpleColor1, 
                             bgcolor=colors.purpleColor8, 
                             pressColor=colors.purpleColor4, 
                             mouseInColor=colors.purpleColor2)
        self.start.y = 0
        self.start.on_click = startGame
        
        self.options = GnuChanGE().gButton(text="Options", scaleX=.25, scaleY=.10, textScale=.1,
                             tcolor=colors.purpleColor1, 
                             bgcolor=colors.purpleColor8, 
                             pressColor=colors.purpleColor4, 
                             mouseInColor=colors.purpleColor2)
        self.options.y = -.15
        self.options.on_click = options

        self.exit = GnuChanGE().gButton(text="Exit", scaleX=.25, scaleY=.10, textScale=.1,
                             tcolor=colors.purpleColor1, 
                             bgcolor=colors.purpleColor8, 
                             pressColor=colors.purpleColor4, 
                             mouseInColor=colors.purpleColor2)
        self.exit.y = -.3
        self.exit.on_click = exit

        self.mainMenuCam = camera

if __name__ == "__main__":
    gc = GnuChanGE()
    MainMenu()
    gc.runLoop()
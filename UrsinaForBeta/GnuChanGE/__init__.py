from ursina import *
from ursina.shaders import lit_with_shadows_shader



class GFunc():
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.delay = 0
        self.finished = False

    def __call__ (self):
        self.finished = True
        return self.func(*self.args, **self.kwargs)

class GColors:
    def __init__(self) -> None:

        # gnuchan Colors purple
        self.gnuchanColor = color.hex("#9d4edd")
        self.gnuchanColor2 = color.hex("#240046")
        self.gnuchanColor3 = color.hex("#3c096c")
        self.gnuchanColor4 = color.hex("#5a189a")

        # Red Colors and Shades
        self.redColor1 = color.hex("#FF0000")
        self.redColor2 = color.hex("#FF4500")
        self.redColor3 = color.hex("#DC143C")
        self.redColor4 = color.hex("#FF6347")
        self.redColor5 = color.hex("#FFA07A")
        self.redColor6 = color.hex("#B22222")
        self.redColor7 = color.hex("#FF0000")
        self.redColor8 = color.hex("#8B0000")

        # Green Colors and Shades
        self.greenColor1 = color.hex("#008000")
        self.greenColor2 = color.hex("#00FF00")
        self.greenColor3 = color.hex("#7FFF00")
        self.greenColor4 = color.hex("#228B22")
        self.greenColor5 = color.hex("#32CD32")
        self.greenColor6 = color.hex("#ADFF2F")
        self.greenColor7 = color.hex("#556B2F")
        self.greenColor8 = color.hex("#008B8B")

        # Blue Colors and Shades
        self.blueColor1 = color.hex("#0000FF")
        self.blueColor2 = color.hex("#000080")
        self.blueColor3 = color.hex("#87CEEB")
        self.blueColor4 = color.hex("#00008B")
        self.blueColor5 = color.hex("#ADD8E6")
        self.blueColor6 = color.hex("#1E90FF")
        self.blueColor7 = color.hex("#0000CD")
        self.blueColor8 = color.hex("#191970")

        # Yellow Colors and Shades
        self.yellowColor1 = color.hex("#FFFF00")
        self.yellowColor2 = color.hex("#FFD700")
        self.yellowColor3 = color.hex("#FFA500")
        self.yellowColor4 = color.hex("#FFC0CB")
        self.yellowColor5 = color.hex("#FF4500")
        self.yellowColor6 = color.hex("#FF6347")
        self.yellowColor7 = color.hex("#FFFFE0")
        self.yellowColor8 = color.hex("#FFFF66")

        # Orange Colors and Shades
        self.orangeColor1 = color.hex("#FFA500")
        self.orangeColor2 = color.hex("#FF4500")
        self.orangeColor3 = color.hex("#FF6347")
        self.orangeColor4 = color.hex("#FF8C00")
        self.orangeColor5 = color.hex("#FF7F50")
        self.orangeColor6 = color.hex("#FFA07A")
        self.orangeColor7 = color.hex("#FFD700")
        self.orangeColor8 = color.hex("#FFB6C1")

        # Navy Colors and Shades
        self.navyColor1 = color.hex("#000080")
        self.navyColor2 = color.hex("#00008B")
        self.navyColor3 = color.hex("#0000CD")
        self.navyColor4 = color.hex("#0000FF")
        self.navyColor5 = color.hex("#000066")
        self.navyColor6 = color.hex("#000044")
        self.navyColor7 = color.hex("#191970")
        self.navyColor8 = color.hex("#333399")

        # Pink Colors and Shades
        self.pinkColor1 = color.hex("#FFC0CB")
        self.pinkColor2 = color.hex("#FF69B4")
        self.pinkColor3 = color.hex("#FF1493")
        self.pinkColor4 = color.hex("#DB7093")
        self.pinkColor5 = color.hex("#C71585")
        self.pinkColor6 = color.hex("#FFB6C1")
        self.pinkColor7 = color.hex("#FFC0CB")
        self.pinkColor8 = color.hex("#FF69B4")

        # Purple Colors and Shades
        self.purpleColor1 = color.hex("#800080")
        self.purpleColor2 = color.hex("#8A2BE2")
        self.purpleColor3 = color.hex("#9932CC")
        self.purpleColor4 = color.hex("#9400D3")
        self.purpleColor5 = color.hex("#800080")
        self.purpleColor6 = color.hex("#9370DB")
        self.purpleColor7 = color.hex("#8A2BE2")
        self.purpleColor8 = color.hex("#9932CC")

        # Turquoise Colors and Shades
        self.turquoiseColor1 = color.hex("#40E0D0")
        self.turquoiseColor2 = color.hex("#00CED1")
        self.turquoiseColor3 = color.hex("#20B2AA")
        self.turquoiseColor4 = color.hex("#008B8B")
        self.turquoiseColor5 = color.hex("#00FFFF")
        self.turquoiseColor6 = color.hex("#00CED1")
        self.turquoiseColor7 = color.hex("#20B2AA")
        self.turquoiseColor8 = color.hex("#008B8B")

        # Gray Colors and Shades
        self.grayColor1 = color.hex("#808080")
        self.grayColor2 = color.hex("#A9A9A9")
        self.grayColor3 = color.hex("#C0C0C0")
        self.grayColor4 = color.hex("#D3D3D3")
        self.grayColor5 = color.hex("#DCDCDC")
        self.grayColor6 = color.hex("#F5F5F5")
        self.grayColor7 = color.hex("#696969")
        self.grayColor8 = color.hex("#2F4F4F")

        # Black and White
        self.blackColor = color.hex("#000000")
        self.whiteColor = color.hex("#FFFFFF")

    def gColorHex(self, colorHexCode=None):
        return color.hex(colorHexCode)

# main game engine 
class GnuChanGE(Entity):
    def __init__(self, title="Default Window Text", borderless=False, developmentMode=False, showSplash=False, vsync=False):
        self.engine = Ursina(title=title, borderless=borderless, development_mode=developmentMode, show_ursina_splash=showSplash, vsync=vsync)
        window.fullscreen = False
        window.size = (1152,648)
    def runLoop(self):
        self.engine.run()

    # Entitiys
    def gEntitiy(self,model=None, parent=None, texture=None, color=color.white, collider=None,
                 x=0, z=0, y=0, origin=(0,0,0), rotationX=0, rotationZ=0, rotationY=0, scaleX=1, scaleY=1, scaleZ=1):
        self.baseObject = Entity(model=model, collider=collider, parent=parent, texture=texture, color=color,
                                 x=x, z=z, y=y, rotation_x=rotationX, rotation_z=rotationZ, rotation_y=rotationY, 
                                 scale_x=scaleX, scale_z=scaleZ, scale_y=scaleY, origin=origin, shader=lit_with_shadows_shader)
        return self.baseObject
    def gPanel(self, bg=GColors().blackColor, scaleX=.5, scaleY=.53, y=.15, x=0):
        self.bg = GnuChanGE().gEntitiy(parent=camera.ui, model="quad", rotationZ=-90,  color=bg, scaleX=scaleY, scaleY=scaleX, y=-y, x=x)
        self.bg.shader = None
        return self.bg
    def gButton(self, parent=camera.ui, text="", y=0, x=0, scaleX=1, scaleY=1, textScale=.35, bRadius=0,
                 tcolor=color.white, bgcolor=color.black, pressColor=color.black66, mouseInColor=color.gray):
        Text.size = textScale
        self.gbutton = Button(parent=parent, text=text, text_origin=(0,0), radius=bRadius,
                              color=bgcolor, pressed_color=pressColor, highlight_color=mouseInColor,
                              scale=(scaleX, scaleY), x=x, y=y)
        self.gbutton.text_entity.world_scale = .35
        self.gbutton.text_entity.color = tcolor
        return self.gbutton
    def gText(self, parent=camera.ui, text="Default Text", textSize=1, textColor=color.white, x=0, y=0):
        self.gtext = Text(parent=parent, text=text, color=textColor, x=x, y=y)
        return self.gtext
    def gMouseInfo(self, text="This is test Text", color=color.white, bg=color.black, wordwrap=50):
        self.gmouseinfo = Tooltip(text=text, background_color=bg, color=color)
        self.gmouseinfo.enabled = True
        return self.gmouseinfo
    def gSlider(self, text="test text", valuChanger=None, vertical=True, x=0, y=0, stepby=1, defaultNumber=5,
                maxNumber=10, minNumer=0):
        self.gslider = Slider(text=text, dynamic=True, on_value_changed=valuChanger, vertical=vertical,
                              x=x, y=y, step=stepby, default=defaultNumber, max=maxNumber, min=minNumer)
        if self.gslider.vertical == True:
            self.gslider.label.rotation_z = 90
            self.gslider.label.origin = (0,0)
            self.gslider.label.position = (.55, .01)
            self.gslider.origin = (.5,0)
            self.newText = ""
            for i in range(0, len(self.gslider.label.text), 15):
                self.newText += text[i:i+15] + "\n"
            self.gslider.label.text = self.newText
        else:
            self.gslider.label.rotation_z = 0
            self.gslider.label.origin = (0,0)
            self.gslider.label.position = (.25, -.04)
            self.gslider.origin = (0,0)

            self.newText = ""
            for i in range(0, len(self.gslider.label.text), 15):
                self.newText += text[i:i+15] + "\n"
            self.gslider.label.text = self.newText
        """
        def boxScaleY():
            box.scale_y = gSlider.value
        """
        return self.gslider



class gAudio(Entity):
    def __init__(self, audioFile=None, autoplay=False,
                 add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        self.gaudio = Audio(sound_file_name=audioFile, auto_destroy=False, autoplay=autoplay)
        self.gaudioStop = False
        self.gaudioPlay = False
        self.gaudioPause = False
    def play(self):
        self.gaudioStop = False
        return self.gaudio.play()
    def stop(self):
        self.gaudioStop = True
        return self.gaudio.stop(destroy=True)
    def pause(self):
        if self.gaudioStop == False and self.gaudioPause == False:
            self.gaudioPause = True
            return self.gaudio.pause()
    def resume(self):
        if self.gaudioStop == False and self.gaudioPause == True:
            self.gaudioPause = False
            return self.gaudio.resume()




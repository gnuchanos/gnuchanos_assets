from ursina import *
from ursina.shaders import lit_with_shadows_shader

class GnuChanGE:
    def __init__(self, title="GnuChanGE Default Text", icon="", borderless=False, developmentMode=True, showSplash=True, 
                 vsync=False) -> None:
        window.icon = icon
        self.engine = Ursina(title=title, borderless=borderless, development_mode=developmentMode, show_ursina_splash=showSplash,
                             vsync=vsync)

    def RunLoop(self):
        self.engine.run()

class GnuchanBeta:
    def __init__(self) -> None:
        pass
    
class GObject:
    def __init__(self, model="", parent="", texture="", color=color.white, 
                 x=0, z=0, y=0, origin=(0,0,0),
                 rotationX=0, rotationZ=0, rotationY=0) -> None:
        self.object = Entity()

        self.object.shader=lit_with_shadows_shader
        
        self.object.model = model
        self.object.parent = parent
        self.object.texture = texture
        self.object.color = color

        self.object.x = x
        self.object.y = y
        self.object.z = z

        self.object.rotation_x = rotationX
        self.object.rotation_y = rotationY
        self.object.rotation_z = rotationZ

        self.object.origin = origin

    @property
    def Create(self):
        return self.object




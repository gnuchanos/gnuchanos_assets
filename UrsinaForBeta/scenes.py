from GnuChanGE import *
from vPlayer import *

class studio(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        # level models
        self.studioCollider = GnuChanGE().gEntitiy(model="models/levels/studio/studio_collider.obj", collider="mesh", color=color.white, texture="color_atlas", rotationY=180)
        self.studioNotCollider = GnuChanGE().gEntitiy(model="models/levels/studio/studio_no_collider.obj", color=color.white, texture="color_atlas", rotationY=180)
        self.studioScreen = GnuChanGE().gEntitiy(model="models/levels/studio/studio_screen.obj", collider="mesh", color=color.white, texture="greenscreen", rotationY=180)
        
        # portal
        self.portal = GnuChanGE().gEntitiy(model="models/extraObjects/portal.obj", texture="color_atlas", collider="box", x=5.5, z=-15)

        # light
        self.point = GnuChanGE().gEntitiy(y=2, z=-10)
        self.lightP = PointLight(parent=self.point, shadow=True)

        # camera
        self.cam = camera
        self.cam.y = 2
        self.cam.z = -55


        # this is player
        self.player = GnuChanPlayer()
        # player model
        self.player.model = GnuChanOSNV()
        
        # for area triger
        self.player.ignore_list = [self.player, self.portal]


    def update(self):
        # change player model
        if held_keys["f"]:
            self.player.model = GnuChanOSNV()
        elif held_keys["g"]:
            self.player.model = GnuChanOsBeta()

        # camera move
        if held_keys["up arrow"]:
            self.cam.z += 10 * time.dt
        elif held_keys["down arrow"]:
            self.cam.z -= 10 * time.dt

        # change level area
        if self.player.intersects(self.portal):
            scene.clear()
            workshop()



class workshop(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        # level models
        self.workshopCollider = GnuChanGE().gEntitiy(model="models/levels/workshop/workshop_collider.obj", collider="mesh", color=color.white, texture="color_atlas", rotationY=180)
        self.workshopNotCollider = GnuChanGE().gEntitiy(model="models/levels/workshop/workshop_no_collider.obj", color=color.white, texture="color_atlas", rotationY=180)

        # portal
        self.portal = GnuChanGE().gEntitiy(model="models/extraObjects/portal.obj", texture="color_atlas", collider="box", x=5.5, z=-15)

        # this is player
        self.player = GnuChanPlayer()
        # player model
        global gnBETA, gnNV
        self.player.model = GnuChanOSNV()



        # light
        self.point = GnuChanGE().gEntitiy(y=5, z=-10, model="cube")
        self.lightP = PointLight(parent=self.point, shadow=True)

        # camera
        self.cam = camera
        self.cam.y = 2
        self.cam.z = -85

        # for area triger
        self.player.ignore_list = [self.player, self.portal]

    def update(self):
        # change player model
        if held_keys["f"]:
            self.player.model = GnuChanOSNV()
        elif held_keys["g"]:
            self.player.model = GnuChanOsBeta()

        # camera move
        if held_keys["up arrow"]:
            self.cam.z += 10 * time.dt
        elif held_keys["down arrow"]:
            self.cam.z -= 10 * time.dt

        # change level area
        if self.player.intersects(self.portal):
            scene.clear()
            studio()



if __name__ == "__main__":
    gc = GnuChanGE()
    workshop()
    gc.runLoop()
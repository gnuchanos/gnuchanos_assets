from GnuChanGE import *
from direct.actor.Actor import Actor







class GnuChanPlayer(Entity):
    def __init__(self, rotationWay="", rotationobj=Entity(), add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        self.rotationWay = rotationWay
        self.objeRotation = rotationobj
        self.origin = (0, 0, 0)
        self.y = 2

        self.height = 1
        self.gravity = 1
        self.grounded = False

        self.collider = "box"
        self.box = GnuChanGE().gEntitiy(model="cube", texture="white_cube")
        self.box.alpha=0.5

        self.traverse_target = scene  # by default, it will collide with everything. change this to change the raycasts' traverse targets.
        self.ignore_list = [self, ]
        if self.gravity:
            self.update_gravity()

    def update(self):
        # move
        self.direction = Vec3(
            self.forward * (held_keys['s'] - held_keys['w'])
            + self.right * (held_keys['q'] - held_keys['e'])
        ).normalized() 

        origin = self.world_position + (self.up * 0.5)
        self.hit_info = raycast(origin, self.direction, ignore=self.ignore_list, distance=1.9, debug=False)

        if not self.hit_info.hit:
            self.position += self.direction * 10 * time.dt

        # rotate player
        self.rotation_y -= held_keys["a"] * 200 * time.dt
        self.rotation_y += held_keys["d"] * 200 * time.dt
      
        # rotate object
        if self.rotationWay != "":
            if self.rotationWay == "x":
                if held_keys["w"]:
                    self.objeRotation.rotation_x += 90 * time.dt
                if held_keys["s"]:
                    self.objeRotation.rotation_x -= 98 * time.dt
            elif self.rotationWay == "y":
                self.objeRotation.rotation_y += 90 * time.dt

        # apple
        if self.gravity:
            self.update_gravity()

    def update_gravity(self):
        self.ray = raycast(self.world_position + (0, self.height, 0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
        if self.ray.hit:
            self.y = self.ray.world_point.y + 0.5
            self.box.position = self.position
            #print("yes ray hit now")


class Animation(Entity):
    def __init__(self, model=None, defaultAnimation=None,
                 add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        self.actor = Actor(model)
        self.actor.reparent_to(self)
        self.defaultAnimation = defaultAnimation
        
    def defaultAnim(self):
        self.actor.loop(self.defaultAnimation)
        return self.actor


class GnuChanOsBeta(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        # GnuChanOS beta
        self.betaParent = self
        self.betaParent.y = -1.02

        self.betaAnimBody = Animation(parent=self.betaParent, model="models/players/GnuChanOS_Beta/model/gnuchanos_ch_purple.gltf", defaultAnimation="idl_loop", shader=lit_with_shadows_shader).defaultAnim()
        # no animation object must be obj
        self.betaAnimFace = GnuChanGE().gEntitiy(parent=self.betaParent, model="models/players/GnuChanOS_Beta/model/gnuchanos_ch_purple_face.obj", texture="normal_face", z=-.01, rotationY=180)
        self.betaAnimFace.shader = lit_with_shadows_shader
        self.betaAnimRotate = GnuChanGE().gEntitiy(parent=self.betaParent, model="models/players/GnuChanOS_Beta/model/gnuchanos_ch_purple_rotation.obj", texture="color_atlas")
        self.betaAnimRotate.shader = lit_with_shadows_shader
    def update(self):
        self.betaAnimRotate.rotation_y += 190 * time.dt
        if held_keys["left mouse"]:
            self.betaAnimBody.loop("idl_tablet_loop")
        if held_keys["right mouse"]:
            self.betaAnimBody.loop("idl_think_loop")
        if held_keys["middle mouse"]:
            self.betaAnimBody.loop("idl_loop")

        if held_keys["1"]:
            self.betaAnimFace.texture = "normal_face"
        if held_keys["2"]:
            self.betaAnimFace.texture = "what_face"
        if held_keys["3"]:
            self.betaAnimFace.texture = "wtf_face"
        if held_keys["4"]:
            self.betaAnimFace.texture = "fear_face"


class GnuChanOSNV(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        # GnuChanOs New Vegas
        self.NVParent = self
        self.NVParent.y = 1.01

        self.NVAnimBody = Animation(parent=self.NVParent, model="models/players/GnuChanOS_nv/model/NVGnuChanOS.gltf", defaultAnimation="idl_loop", shader=lit_with_shadows_shader).defaultAnim()
        self.NVAnimFace = Animation(parent=self.NVParent, model="models/players/GnuChanOS_nv/model/NVGnuChanOS_face.gltf", defaultAnimation="idl_loop", shader=lit_with_shadows_shader).defaultAnim()
        # not animation object must be obj
        self.NVAnimRotate = GnuChanGE().gEntitiy(parent=self.NVParent, model="models/players/GnuChanOS_nv/model/nvWheel.obj", texture="color_atlas", y=-.95)
        self.NVAnimRotate.shader = lit_with_shadows_shader

    def update(self):
        if held_keys["w"]:
            self.NVAnimRotate.rotation_x -= 190 * time.dt
        if held_keys["s"]:
            self.NVAnimRotate.rotation_x += 190 * time.dt
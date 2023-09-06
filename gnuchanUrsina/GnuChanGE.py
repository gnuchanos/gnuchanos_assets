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
        self.jump_height = 2
        self.jump_up_duration = 0.5
        self.fall_after = 0.35  # will interrupt jump up
        self.jumping = False
        self.air_time = 0

        self.traverse_target = scene  # by default, it will collide with everything. change this to change the raycasts' traverse targets.
        self.ignore_list = [self, ]
        if self.gravity:
            self.update_gravity()

    def update_gravity(self):
        ray = raycast(self.world_position + (0, self.height, 0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
        if ray.hit:
            self.y = ray.world_point.y
            print("yes ray hit now")

    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['s'] - held_keys['w'])
            + self.right * (held_keys['q'] - held_keys['e'])
        ).normalized()  # get the direction we're trying to walk in.

        self.rotation_y -= held_keys["a"] * 200 * time.dt
        self.rotation_y += held_keys["d"] * 200 * time.dt

        origin = self.world_position + (self.up * 0.5)  # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin, self.direction, ignore=(self,), distance=0.5, debug=False)

        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt

        if self.rotationWay == "x":
            if held_keys["w"]:
                self.objeRotation.rotation_x += 90 * time.dt
            if held_keys["s"]:
                self.objeRotation.rotation_x -= 98 * time.dt
        elif self.rotationWay == "y":
            self.objeRotation.rotation_y += 90 * time.dt

        if self.gravity:
            self.update_gravity()

    def input(self, key):
        if key == 'space':
            self.jump()

    def jump(self):
        if not self.grounded:
            return

    def land(self):
        self.air_time = 0
        self.grounded = True


    
class GObject:
    def __init__(self, model="", parent="", texture="", color=color.white, collider="",
                 x=0, z=0, y=0, origin=(0,0,0),
                 rotationX=0, rotationZ=0, rotationY=0) -> None:
        self.object = Entity()

        self.object.shader=lit_with_shadows_shader
        
        self.object.model = model
        self.object.collider = collider
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




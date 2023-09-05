from GnuChanGE import *

gc = GnuChanGE(icon="icon.ico")



gnuchanos_nv = GObject(z=-4, y=.5, rotationY=180).Create
gnuchanos_nv_body = GObject(parent=gnuchanos_nv, model="gnuchanoıs_fnv_sec", texture="color_atlas", y=-.2).Create
gnuchanos_nv_wheel = GObject(parent=gnuchanos_nv, model="gnuchanoıs_fnv_sec_wheel", texture="color_atlas", y=.1).Create

workshop = GObject(model="workshop", texture="color_atlas", rotationY=180).Create


cam = camera
cam.y = 3
cam.z = -25

lightPoint = GObject(y=5, z=-8)
light = PointLight(parent=lightPoint, shadow=True)

move_speed = 5
def update():
    forward = gnuchanos_nv.forward

    gnuchanos_nv.rotation_y -= held_keys["a"] * 200 * time.dt
    gnuchanos_nv.rotation_y += held_keys["d"] * 200 * time.dt
    
    gnuchanos_nv_wheel.rotation_x += held_keys["w"] * 190 * time.dt
    gnuchanos_nv_wheel.rotation_x -= held_keys["s"] * 190 * time.dt

    gnuchanos_nv.x += forward.x * (held_keys['w'] - held_keys['s']) * move_speed * time.dt
    gnuchanos_nv.z += forward.z * (held_keys['w'] - held_keys['s']) * move_speed * time.dt

    

gc.RunLoop()
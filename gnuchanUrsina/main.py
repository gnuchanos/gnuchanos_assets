from GnuChanGE import *



gc = GnuChanGE(icon="icon.ico")


# GnuChanBeta Player Model
gnuchanos_nv = GObject(z=-4, rotationY=180).Create
gnuchanos_nv_body = GObject(parent=gnuchanos_nv, model="gnuchanoıs_fnv_sec", texture="color_atlas").Create
gnuchanos_nv_wheel = GObject(parent=gnuchanos_nv, model="gnuchanoıs_fnv_sec_wheel", texture="color_atlas").Create
gnuchanos_nv_face = GObject(parent=gnuchanos_nv, model="gnuchanoıs_fnv_face", texture="gnuchanos_nv_face_huseyin").Create


# level design
workshop = GObject(model="workshop", texture="color_atlas", rotationY=180, collider="mesh").Create

# player must be this place
GnuChanPlayer(model=gnuchanos_nv, rotationWay="x", rotationobj=gnuchanos_nv_wheel)


#camera
cam = camera
cam.y = 3
cam.z = -25

# light
lightPoint = GObject(y=5, z=-8)
light = PointLight(parent=lightPoint, shadow=True)




def update():
    if held_keys["up arrow"]:
        cam.z += 5 * time.dt
    elif held_keys["down arrow"]:
        cam.z -= 5 * time.dt
    

gc.RunLoop()
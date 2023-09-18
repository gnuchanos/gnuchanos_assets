extends Node


# change texture
var material_instance : SpatialMaterial
func _ready():
	# Önce material_instance'ı elde ediyoruz
	material_instance = load("res://default_DataFiles/3d/workshop/logo.material") as SpatialMaterial
	var new_albedo_texture : Texture = load("res://default_DataFiles/3d/workshop/faceEmpty.png")
	material_instance.albedo_texture = new_albedo_texture

func _process(delta):
	var new_albedo_texture : Texture = load("res://default_DataFiles/FPS/3dgc/gnuchan_nw/gnuchanos_nv_face_huseyin.png")
	material_instance.albedo_texture = new_albedo_texture
########################################################################################################################


# animation 
var playback : AnimationNodeStateMachinePlayback
func _ready():
	playback = get("parameters/playback")
	playback.start("idl_loop")
	active = true

func _process(_delta):
	if Input.is_action_pressed("left_m"):
		playback.travel("idl_tablet_loop")
########################################################################################################################

# raycast hit
onready var raycast = $Camera3D/RayCast3D
func _process(delta):
	if raycast.is_colliding():
		var collider = raycast.get_collider() # collider
		if collider.name in ["p1", "p2", "p3"]: # object list
			if Input.is_action_pressed("left_m"):
				collider.rotation.y += 1 * delta # rotate
						.scale += Vector3(0, 0.1, 0) #scale
						.position.x += 1 * delta # move #translation.z godot3 | position is godot4



# raycast projectile
onready var shootPointLeft = $RayCast/leftShootAim #Empty node for aim
const LEFT_BULLET = preload("res://PlayerBullet.tscn") # 3d bullet and area
# bullet shot but not move just projectile
func _process(delta):
	if xraycast.is_colliding():
		if Input.is_action_pressed("leftM"):
			var collider = xraycast.get_collider() # collider
			if collider.name in "enemy":
				if second >= 0:
					second -= delta
				else:
					var LeftBullet = LEFT_BULLET.instance()
					get_parent().add_child(LeftBullet)
					LeftBullet.global_transform = shootPointLeft.global_transform


00# bullet projetile script example
var areaEnter = false
var speed = 50
# bullet hit and damage
func _process(delta):
	if areaEnter == true:
		Global.enemyHealth -= 2 # if player in bullet area this mean hit
		self.queue_free() # and remove bullet
	else:
		# Mermiyi sadece ileri yönde hareket ettir
		translation += Vector3(0, 0, -speed * delta)  # if not hit bullet can move # this is player
		#bullet.global_transform = shootPoint.global_transform # this is normal # this is not move correct in player

func _on_PlayerBullet_body_entered(body): # area
	if body.name == "enemy":
		areaEnter = true


########################################################################################################################

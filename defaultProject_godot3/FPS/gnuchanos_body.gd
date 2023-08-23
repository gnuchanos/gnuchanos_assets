extends Spatial

var material_instance : SpatialMaterial

func _ready():
	# Önce material_instance'ı elde ediyoruz
	material_instance = load("res://FPS/3dgc/gnuchan_proto/face.material") as SpatialMaterial



	var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/agla_face.png")
	material_instance.albedo_texture = new_albedo_texture




func _process(delta):
	$gnuchanos_beta/gnuchanos_beta1/Skeleton/rotate.rotate_y(deg2rad(90) * delta)

	if Input.is_action_just_pressed("1"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/agla_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("2"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/fear_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("3"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/happy_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("4"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/ilkill_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("5"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/normal_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("6"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/what_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("7"):
		var new_albedo_texture : Texture = load("res://FPS/3dgc/gnuchan_proto/face/wtf_face.png")
		material_instance.albedo_texture = new_albedo_texture

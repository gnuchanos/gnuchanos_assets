extends Spatial

var material_instance : SpatialMaterial
var face = false
func _ready():
	# Önce material_instance'ı elde ediyoruz
	material_instance = load("res://default_DataFiles/3d/workshop/logo.material") as SpatialMaterial
	var new_albedo_texture : Texture = load("res://default_DataFiles/3d/workshop/faceEmpty.png")
	material_instance.albedo_texture = new_albedo_texture

func _process(delta):

	if face == false:
		if Input.is_action_just_pressed("f") :
			var new_albedo_texture : Texture = load("res://default_DataFiles/FPS/3dgc/gnuchan_nw/gnuchanos_nv_face_huseyin.png")
			material_instance.albedo_texture = new_albedo_texture
			face = true
			print(face)
	else:
		if Input.is_action_just_pressed("f") and face == true:
			var new_albedo_texture : Texture = load("res://default_DataFiles/3d/workshop/faceEmpty.png")
			material_instance.albedo_texture = new_albedo_texture
			face = false
			print(face)

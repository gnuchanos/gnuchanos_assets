extends Spatial


var material_instance : SpatialMaterial
func _ready():
	# Önce material_instance'ı elde ediyoruz
	material_instance = load("res://data/3d/players/gnuchanBeta/face.material") as SpatialMaterial
	var new_albedo_texture : Texture = load("res://data/3d/players/gnuchanBeta/face/normal_face.png")
	material_instance.albedo_texture = new_albedo_texture

func _process(delta):

	$rotate.rotate_y(90*delta)

	if Input.is_action_just_pressed("1"):
		var new_albedo_texture : Texture = load("res://data/3d/players/gnuchanBeta/face/normal_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("2"):
		var new_albedo_texture : Texture = load("res://data/3d/players/gnuchanBeta/face/fear_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("3"):
		var new_albedo_texture : Texture = load("res://data/3d/players/gnuchanBeta/face/what_face.png")
		material_instance.albedo_texture = new_albedo_texture
	if Input.is_action_just_pressed("4"):
		var new_albedo_texture : Texture = load("res://data/3d/players/gnuchanBeta/face/wtf_face.png")
		material_instance.albedo_texture = new_albedo_texture

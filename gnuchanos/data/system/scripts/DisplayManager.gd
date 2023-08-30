extends Control


@onready var inputName =  $login/VBoxContainer/userName
@onready var inputPassword = $login/VBoxContainer/password



func  _ready():
	inputName.grab_focus()

func _process(delta):
	if Input.is_action_just_pressed("enter"):
		if inputName.text == inputPassword.text:
			get_tree().change_scene_to_file("res://data/system/WindowManager.tscn")

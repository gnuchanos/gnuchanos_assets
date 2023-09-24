extends Control

@onready var userName = $loginPanel/panel/userName
@onready var userPassword = $loginPanel/panel/userPassword

func _process(delta):
	if Input.is_action_just_pressed("enter"):
		if userName.text != "" and userPassword.text != "":
			get_tree().change_scene_to_file("res://data/systemPrograms/WindowManager.tscn")

extends Control

onready var userName = $loginPanel/VBoxContainer/userName
onready var userPassword = $loginPanel/VBoxContainer/userPassword
onready var warning = $loginPanel/VBoxContainer/warn

func _ready():
	userName.grab_focus()


func _process(delta):
	if Input.is_action_just_pressed("enter"):
		if userName.text != "" and userPassword.text != "":
			get_tree().change_scene("res://data/systemLevel/windowManager.tscn")
		else:
			warning.text = "user password or name is empty"

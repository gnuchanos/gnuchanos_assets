extends Control

onready var username = $userName/userNane
onready var userpassword = $userPassword/userPassword

func _ready():
	pass

func _on_login_pressed():
	if username.text == "user13":
		if userpassword.text == "123":
			get_tree().change_scene("res://GUI/mainScreen.tscn")

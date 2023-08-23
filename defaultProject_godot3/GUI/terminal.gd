extends Control

onready var lineInput = $WindowDialog/Control/VBoxContainer/LineEdit
onready var multiLineInput = $WindowDialog/Control/VBoxContainer/TextEdit





func _process(delta):
	if Input.is_action_just_pressed("enter"):
		multiLineInput.text += lineInput.text + "\n"


		if lineInput.text == "studio":
			get_tree().change_scene("res://levels/levelStudio.tscn")




		lineInput.text = ""

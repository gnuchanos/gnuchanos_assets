extends Control

onready var lineInput = $WindowDialog/Control/VBoxContainer/LineEdit
onready var multiLineInput = $WindowDialog/Control/VBoxContainer/TextEdit





func _process(delta):
	if Input.is_action_just_pressed("enter"):
		multiLineInput.text += lineInput.text + "\n"


		if lineInput.text == "studio":
			get_tree().change_scene("res://default_DataFiles/levels/levelStudio.tscn")
		elif lineInput.text == "workshop":
			get_tree().change_scene("res://default_DataFiles/levels/workshop.tscn")




		lineInput.text = ""

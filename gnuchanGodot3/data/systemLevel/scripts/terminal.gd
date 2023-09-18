extends WindowDialog


onready var TOutput = $bg/VBoxContainer/terminalOutput
onready var tInput = $bg/VBoxContainer/input

func _process(delta):
	if Input.is_action_just_pressed("enter"):
		TOutput.text += tInput.text + "\n"
		if tInput.text == "workshop":
			get_tree().change_scene("res://data/levels/workshop.tscn")

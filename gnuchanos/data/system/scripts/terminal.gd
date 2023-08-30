extends Control

@onready var input = $Window/VBoxContainer/input
@onready var terminal = $Window/VBoxContainer/terminal


func _process(_delta):
	if Input.is_action_just_pressed("altEnter"):
		$Window.show()
	if Input.is_action_just_pressed("enter"):
		terminal.text += input.text + "\n"
		if input.text == "studio":
			get_tree().change_scene_to_file("res://data/levels/studio.tscn")
		elif input.text == "workshop":
			get_tree().change_scene_to_file("res://data/levels/workshop.tscn")
		input.text = ""
	input.grab_focus()



func _on_window_close_requested():
	$Window.hide()
	$Window/VBoxContainer/input.text = ""
	$Window/VBoxContainer/terminal.text = ""

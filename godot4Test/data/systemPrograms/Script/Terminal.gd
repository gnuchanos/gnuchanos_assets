extends Window


@onready var output = $bg/VBoxContainer/output
@onready var input = $bg/VBoxContainer/input


func _process(delta):
	if Input.is_action_just_pressed("ui_accept"):
		output.text += input.text + "\n"






		input.text = ""

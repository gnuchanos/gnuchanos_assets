extends Control


func _process(delta):
	if Input.is_action_just_pressed("altEnter"):
		$programs/terminal.popup_centered()

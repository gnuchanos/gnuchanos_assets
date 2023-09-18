extends Control


func _process(delta):
	if Input.is_action_just_pressed("altEnter"):
		$programs/WindowDialog.popup_centered()

extends Camera








func _process(delta):
	if Input.is_action_pressed("ui_up"):
		self.translation.z -= 3 * delta
	if Input.is_action_pressed("ui_down"):
		self.translation.z += 3 * delta
extends Camera3D


func _process(delta):
	if Input.is_action_pressed("ui_up"):
		self.position.z -= 3 * delta
	if Input.is_action_pressed("ui_down"):
		self.position.z += 3 * delta

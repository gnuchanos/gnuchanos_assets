extends Camera3D


func _process(delta):
	if Input.is_action_pressed("ui_up"):
		self.position.z -= 8 * delta
	elif Input.is_action_pressed("ui_down"):
		self.position.z += 8 * delta

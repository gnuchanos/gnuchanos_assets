extends RayCast






func _physics_process(delta):
	if self.is_colliding():
		var collider = self.get_collider()

		if Input.is_action_just_pressed("left_m"):
			if collider.name == "dynamic":
				$debug.text = "dynamic object"
			if collider.name == "static":
				$debug.text = "this is static object"

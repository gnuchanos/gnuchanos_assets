extends RayCast






func _physics_process(delta):
	if self.is_colliding():
		var collider = self.get_collider()

		if Input.is_action_pressed("e"):
			if collider.name == "dynamic": # kinematicbody
				$debug.text = "dynamic object"
				collider.rotation.y += 90 * delta

			if collider.name == "static": #statickbody
				$debug.text = "this is static object"
				collider.rotation.y += 90 * delta

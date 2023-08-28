extends RayCast






func _physics_process(delta):
	if self.is_colliding():
		var collider = self.get_collider()
		if Input.is_action_pressed("e"):
			pass
	

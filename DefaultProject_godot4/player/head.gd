extends Node3D

@onready var raycast = $Camera3D/RayCast3D

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.




func _process(delta):
	if raycast.is_colliding():
		var collider = raycast.get_collider()

		if collider.name in ["p1", "p2", "p3"]:
			if Input.is_action_pressed("left_m"):
				collider.rotation.y += 10 * delta

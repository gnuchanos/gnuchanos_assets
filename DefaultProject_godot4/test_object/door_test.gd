extends Node3D


var doorOpen = false
var areaEntered = false




func  _process(delta):
	if areaEntered == true:
		if doorOpen == false:
			if Input.is_action_just_pressed("left_m"):
				$AnimationPlayer.play("Open")
				doorOpen = true
		else:
			if Input.is_action_just_pressed("left_m"):
				$AnimationPlayer.play_backwards("Open")
				doorOpen = false


func _on_area_3d_body_entered(body):
	if body.name == "FPS":
		areaEntered = true
func _on_area_3d_body_exited(body):
	if body.name == "FPS":
		areaEntered = false

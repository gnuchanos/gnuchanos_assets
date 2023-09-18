extends Node3D


func  _process(delta):
	$GnuChanOSNV/AnimationPlayer.play("idl")
	if Input.is_action_pressed("w"):
		$GnuChanOSNV/whlee.rotation.x -= 90 * delta
	if Input.is_action_pressed("s"):
		$GnuChanOSNV/whlee.rotation.x += 90 * delta


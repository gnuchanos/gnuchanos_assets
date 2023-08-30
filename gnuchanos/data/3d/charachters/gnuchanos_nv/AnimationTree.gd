extends AnimationTree


var playback : AnimationNodeStateMachinePlayback
func _ready():
	playback = get("parameters/playback")
	playback.start("idl")
	active = true

func _process(_delta):

	if Input.is_action_pressed("w"):
		playback.travel("walk")
	if Input.is_action_just_released("w"):
		playback.travel("idl")

	if Input.is_action_pressed("leftM"):
		playback.travel("idl_bye")
	elif Input.is_action_just_released("leftM"):
		playback.travel("idl")

	if Input.is_action_pressed("rightM"):
		pass
	elif Input.is_action_just_released("rightM"):
		pass

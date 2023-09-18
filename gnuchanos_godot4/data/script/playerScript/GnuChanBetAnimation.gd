extends AnimationTree

var playback : AnimationNodeStateMachinePlayback
func _ready():
	playback = get("parameters/playback")
	playback.start("playerAnimation_idl")
	active = true

func _process(_delta):
	if Input.is_action_pressed("left_m"):
		playback.travel("playerAnimation_idl_tablet")
	elif  Input.is_action_just_released("left_m"):
		playback.travel("playerAnimation_idl")

	if Input.is_action_pressed("right_m"):
		playback.travel("playerAnimation_idl_think")
	elif  Input.is_action_just_released("right_m"):
		playback.travel("playerAnimation_idl")

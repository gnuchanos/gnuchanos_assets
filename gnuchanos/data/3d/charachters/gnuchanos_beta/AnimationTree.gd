extends AnimationTree


var playback : AnimationNodeStateMachinePlayback
func _ready():
	playback = get("parameters/playback")
	playback.start("idl")
	active = true

func _process(_delta):
	if Input.is_action_pressed("leftM"):
		playback.travel("idl_tablet")
	elif Input.is_action_just_released("leftM"):
		playback.travel("idl_tablet_ends")

	if Input.is_action_pressed("rightM"):
		playback.travel("idl_think")
	elif Input.is_action_just_released("rightM"):
		playback.travel("idl_think_end")

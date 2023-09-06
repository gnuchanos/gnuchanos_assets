extends AnimationTree


var playback : AnimationNodeStateMachinePlayback
func _ready():
	playback = get("parameters/playback")
	playback.start("idl_loop")
	active = true

func _process(_delta):
	if Input.is_action_pressed("left_m"):
		playback.travel("idl_tablet_loop")
	elif Input.is_action_just_released("left_m"):
		playback.travel("idl_loop")
	
	if Input.is_action_pressed("right_m"):
		playback.travel("idl_think_loop")
	elif Input.is_action_just_released("right_m"):
		playback.travel("idl_loop")



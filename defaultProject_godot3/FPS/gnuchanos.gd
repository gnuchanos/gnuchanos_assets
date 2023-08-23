extends KinematicBody


# default script
const ACCEL_DEFAULT = 7
const ACCEL_AIR = 1
onready var accel = ACCEL_DEFAULT
var gravity = 15

var jump = GlobalVar.fpsVar["jump"]

var cam_accel = 40
var mouse_sense = GlobalVar.fpsVar["MouseSensivity"]
var snap

var direction = Vector3()
var velocity = Vector3()
var gravity_vec = Vector3()
var movement = Vector3()
# default Script


# hareket ve koşu
var speed
const WALK_SPEED = 6.5
const  SPRINT_SPEED = 10.0

onready var head = $body
onready var DuckRay = $duckRay
onready var body = $stand
var duck = false


var mouse_sensitivity = 0.15

# defaul script
func _ready():
	#hides the cursor
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	
func _input(event):
	if event is InputEventMouseMotion:
		rotate_y(deg2rad(-event.relative.x * mouse_sensitivity))


func _physics_process(delta):

	# Duck
	if Input.is_action_pressed("ctrl") and is_on_floor():
		body.shape.height -=  15.0 * delta
		duck = true
	else:
		if not DuckRay.is_colliding():
			body.shape.height +=  15.0 * delta
			duck = false
	body.shape.height = clamp(body.shape.height, .05, 2)
	# fast move
	if Input.is_action_pressed("sprint") and is_on_floor():
		speed = SPRINT_SPEED
	else:
		if duck == false:
			speed = WALK_SPEED
		else:
			speed = 3
	####


	# defaul script
	direction = Vector3.ZERO
	var h_rot = global_transform.basis.get_euler().y
	var f_input = Input.get_action_strength("s") - Input.get_action_strength("w")
	var h_input = Input.get_action_strength("d") - Input.get_action_strength("a")
	direction = Vector3(h_input, 0, f_input).rotated(Vector3.UP, h_rot).normalized()

	#jumping and gravity
	if is_on_floor():
		snap = -get_floor_normal()
		accel = ACCEL_DEFAULT
		gravity_vec = Vector3.ZERO
	else:
		snap = Vector3.DOWN
		accel = ACCEL_AIR
		gravity_vec += Vector3.DOWN * gravity * delta

	if Input.is_action_just_pressed("jump") and is_on_floor():
		snap = Vector3.ZERO
		gravity_vec = Vector3.UP * jump
	
	#make it move
	velocity = velocity.linear_interpolate(direction * speed, accel * delta)
	movement = velocity + gravity_vec
	
	move_and_slide_with_snap(movement, snap, Vector3.UP)
	# defaul script

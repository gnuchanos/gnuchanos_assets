extends KinematicBody


# default script
const ACCEL_DEFAULT = 7
const ACCEL_AIR = 1
onready var accel = ACCEL_DEFAULT
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity") # default 9.8 this is godot 4 gravity

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

onready var head = $Head
onready var camera = $Head/Camera
onready var DuckRay = $duckRay
onready var body = $stand
var duck = false

# fov
const  BASE_FOV = 75.0
const FOV_CHANGE = 1.5

var mouse_sensitivity = 0.6

# defaul script
func _ready():
	#hides the cursor
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	
func _input(event):
	if event is InputEventMouseMotion:
		rotate_y(deg2rad(-event.relative.x * mouse_sensitivity))
		head.rotate_x(deg2rad(-event.relative.y * mouse_sensitivity))
		head.rotation.x = clamp(head.rotation.x + deg2rad(-event.relative.y * mouse_sensitivity), deg2rad(-90), deg2rad(90))

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
	$Head/Camera/headRay/debug.text = "X:"+ str(self.translation.x) + " | Z:"+ str(self.translation.z) + " | Y:"+ str(self.translation.y) + " | body.shape.height" + str(body.shape.height)
	# fast move
	if Input.is_action_pressed("sprint") and is_on_floor():
		speed = SPRINT_SPEED
	else:
		if duck == false:
			speed = WALK_SPEED
		else:
			speed = 3
	# FOV
	var velocity_clamped = clamp(velocity.length(), 0.5, SPRINT_SPEED * 2)
	var target_fov = BASE_FOV + FOV_CHANGE * velocity_clamped
	camera.fov = lerp(camera.fov, target_fov, delta * 8.0)
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

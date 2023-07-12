extends CharacterBody3D

# duck
var duck = false
var duckRayHit = false

# hareket ve koşu
var speed
const WALK_SPEED = 5.0
const  SPRINT_SPEED = 10.0

const JUMP_VELOCITY = 4.5
const  MOUSE_SENSITIVTY = 0.01

@onready var head = $head
@onready var camera = $head/Camera3D

# kafa hareketi
const  BOB_FREQ = 2.0
const BOB_AMP = 0.08
var t_bob = 8.8

# fov
const  BASE_FOV = 75.0
const FOV_CHANGE = 1.5

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

#hide mouse
func  _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

# camera and head move
func  _unhandled_input(event):
	if event is InputEventMouseMotion:
		head.rotate_y(-event.relative.x * MOUSE_SENSITIVTY)
		camera.rotate_x(-event.relative.y * MOUSE_SENSITIVTY)
		camera.rotation.x = clamp(camera.rotation.x, deg_to_rad(-60), deg_to_rad(60))
	######

#test debug
func  _process(_delta):
	$debug.text = str(speed)
	######

func _physics_process(delta):
	# gravty and jump
	if not is_on_floor():
		velocity.y -= gravity * delta
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY
	######

	# Duck
	# i don't know how
	#########

	# fast move
	if Input.is_action_pressed("sprint") and is_on_floor():
		speed = SPRINT_SPEED
	else:
		speed = WALK_SPEED

	#move
	var input_dir = Input.get_vector("a", "d", "w", "s")
	var direction = (head.transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x * speed
		velocity.z = direction.z * speed
	else:
		velocity.x = 0.0
		velocity.z = 0.0

	# Head bob
	t_bob += delta * velocity.length() * float(is_on_floor())
	camera.transform.origin = _headbob(t_bob)
	####

	# FOV
	var velocity_clamped = clamp(velocity.length(), 0.5, SPRINT_SPEED * 2)
	var target_fov = BASE_FOV + FOV_CHANGE * velocity_clamped
	camera.fov = lerp(camera.fov, target_fov, delta * 8.0)
	####

	move_and_slide()

# Head bob
func _headbob(time) -> Vector3:
	var pos = Vector3.ZERO
	pos.y = sin(time * BOB_FREQ) * BOB_AMP
	pos.x = cos(time * BOB_FREQ) * BOB_AMP
	return pos 

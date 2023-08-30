extends CharacterBody3D

# hareket ve koşu
var speed
const WALK_SPEED = 5.0
const  SPRINT_SPEED = 10.0

const JUMP_VELOCITY = 4.5
const  MOUSE_SENSITIVTY = 0.005

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

#hide mouse
func  _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

# camera and head move
func  _unhandled_input(event):
	if event is InputEventMouseMotion:
		rotate_y(-event.relative.x * MOUSE_SENSITIVTY)

func _physics_process(delta):
	if Input.is_action_pressed("w"):
		$"gnuchanoıs_fnv_sec/whlee".rotate_x(-90*delta)
	elif Input.is_action_pressed("s"):
		$"gnuchanoıs_fnv_sec/whlee".rotate_x(90*delta)


	# gravty and jump
	if not is_on_floor():
		velocity.y -= gravity * delta
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY
	######

	speed = WALK_SPEED

	#move
	var input_dir = Input.get_vector("a", "d", "w", "s")
	var direction = (self.transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	#var direction = (head.transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x * speed
		velocity.z = direction.z * speed
	else:
		velocity.x = 0.0
		velocity.z = 0.0

	move_and_slide()


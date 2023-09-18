extends Label

var frame_count := 0
var time_passed := 0.0
var update_interval := 1.0  # 1 saniyede bir güncelle

func _ready():
	set_process(true)

func _process(delta):
	frame_count += 1
	time_passed += delta

	if time_passed >= update_interval:
		var fps = frame_count / time_passed
		text = "FPS: " + str(int(fps))
		frame_count = 0
		time_passed = 0.0

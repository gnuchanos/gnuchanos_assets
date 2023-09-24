extends Control


@onready var systemPanel = $bottomBG/bottonhbox/middleSystem
@onready var rightPanel = $topBG/tophbox/rightPanel
@onready var ShortcutInfo = $system/systemInfo


func  _ready():
	ShortcutInfo.text = """
	Terminal: Alt+Enter
	Calculator: Not Finish
	Timer: Not Finish
	Alarm: Not Finish
	Text Editor: Not Finish
	"""



func _process(delta):
	if Input.is_action_just_pressed("ui_accept"):
		$programs/terminal.popup_centered()

func _on_window_close_requested():
	$programs/terminal.hide()

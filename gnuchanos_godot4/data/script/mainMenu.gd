extends Control


func _process(delta):
	pass


func _on_start_game_pressed():
	get_tree().change_scene_to_file("res://data/levels/workshop.tscn")


func _on_options_pressed():
	pass # Replace with function body.


func _on_exit_pressed():
	get_tree().quit()

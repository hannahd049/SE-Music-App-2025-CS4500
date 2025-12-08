extends Sprite2D





func _on_home_button_pressed() -> void:
	print("Home button pressed — stopping music.")
	get_tree().change_scene_to_file("res://UISETitleScreenMusic.tscn")


func _on_play_button_pressed() -> void:
	get_tree().change_scene_to_file("res://ui_si_music_play_screen.tscn") #  res://ui_si_music_blank_template.tscn

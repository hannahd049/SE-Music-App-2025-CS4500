extends Sprite2D


func _on_yourlist_button_pressed() -> void:
	print("your list pressed — stopping music.")
	get_tree().change_scene_to_file("res://your_list_screen.tscn")

func _on_play_button_pressed() -> void:
	get_tree().change_scene_to_file("res://ui_si_music_play_screen.tscn") #res://ui_si_music_blank_template.tscn res://ui_si_music_play_screen.tscn

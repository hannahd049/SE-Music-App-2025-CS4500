class_name UIHelper

static func switch_to_player(node: Node) -> void:
	node.get_tree().change_scene_to_file("res://SongPlayerScreen.tscn")

static func switch_to_home(node: Node) -> void:
	node.get_tree().change_scene_to_file("res://HomeScreen.tscn")
	
static func switch_to_list(node: Node) -> void:
	node.get_tree().change_scene_to_file("res://YourListScreen.tscn")

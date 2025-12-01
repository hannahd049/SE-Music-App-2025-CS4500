extends Node

var api_client: ApiClient = null

func _init() -> void:
	pass
	
func _enter_tree() -> void:
	api_client = get_node("ApiClient")
	get_after_next_frame()

func get_after_next_frame() -> void:
	await get_tree().process_frame
	api_client.get_next_song()

	#todo: request song list from backend
	
func play_presssed() -> void:
	UIHelper.switch_to_player(self)

func home_presssed() -> void:
	UIHelper.switch_to_home(self)

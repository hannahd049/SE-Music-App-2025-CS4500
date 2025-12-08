extends Sprite2D

var api_client: ApiClient = null
var liked_songs: Array = []

func _ready():
	
	api_client = get_node("ApiClient")
	
	request_liked_songs()

func request_liked_songs() -> void:
	var http_request = HTTPRequest.new()
	add_child(http_request)

	
	var endpoint = api_client.apiUrl + "/likedsongs/" + api_client.userId
	var error = http_request.request(endpoint)

	if error != OK:
		print("Failed to request liked songs")
		return


	var response = await http_request.request_completed 
	http_request.queue_free()

	if response[0] == HTTPRequest.RESULT_SUCCESS:
		var json = JSON.new()
		var parse_result = json.parse(response[3].get_string_from_utf8())
		if parse_result == OK:
			liked_songs = json.data
			display_liked_songs()
		else:
			print("Failed to parse liked songs response")
	else:
		print("HTTP request failed")

func display_liked_songs() -> void:
	
	var item_list = get_node_or_null("ItemList")
	if item_list:
		item_list.clear()

		if liked_songs.is_empty():
			item_list.add_item("You haven't liked any songs yet")
			return
		
		# Display each liked song
		for song in liked_songs:
			var display_text = "%s (ID: %d)" % [song["songName"], song["songId"]]
			item_list.add_item(display_text)
	else:
		print("ItemList node not found!")

func _on_home_button_pressed() -> void:
	print("Home button pressed — stopping music.")
	get_tree().change_scene_to_file("res://UISETitleScreenMusic.tscn")

func _on_play_button_pressed() -> void:
	get_tree().change_scene_to_file("res://ui_si_music_blank_template.tscn")

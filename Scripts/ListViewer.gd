extends Node

var api_client: ApiClient = null
var liked_songs: Array =[]

func _init() -> void:
	pass
	
func _enter_tree() -> void:
	api_client = get_node("ApiClient")
	api_client.song_received.connect(_on_song_received)
	get_after_next_frame()

func get_after_next_frame() -> void:
	await get_tree().process_frame
	api_client.get_next_song()
	await request_liked_songs()
	#todo: request song list from backend

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

func display_liked_songs() -> void:
	var item_list = get_node_or_null("ItemList")
	if item_list:
		item_list.clear()

		if liked_songs.is_empty():
			item_list.add_item("You liked no songs yet")
			return
		
		for song in liked_songs:
			var display_text = "%s (ID: %d )" % [song["songName"], song ["songId"]]
			
			item_list.add_item(display_text) 
	
func play_presssed() -> void:
	UIHelper.switch_to_player(self)

func home_presssed() -> void:
	UIHelper.switch_to_home(self)

func _on_song_received(song_name: String, song_id: int, body: PackedByteArray) -> void:
	print("Song Added", song_name)
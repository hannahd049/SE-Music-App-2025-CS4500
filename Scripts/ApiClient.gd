class_name ApiClient
extends Node 

signal song_received

const apiUrl = "http://127.0.0.1:5128/api"
static var userId = "user123" #todo

func init() -> void:
	pass #todo: save/load userid from file

func rate_song(song_id: int, positive: bool):
	var request = HTTPRequest.new()
	add_child(request)
	
	var body = JSON.stringify({"songId": song_id, "positive" : positive, "userId" : userId})
	var error = request.request(apiUrl + "/rs", ["Content-Type: application/json"], HTTPClient.METHOD_POST, body)
	
	if error != OK:
		push_error("Failed to request next song: " + error)
	
func get_next_song():
	var request = HTTPRequest.new()
	add_child(request)
	
	request.request_completed.connect(self._on_response)
	
	var error = request.request(apiUrl + "/ns", [], HTTPClient.METHOD_GET)
	
	if error != OK:
		push_error("Failed to request next song: " + error)
		
func get_thumbnail(song_id: int, sprite: Sprite2D):
	var request = HTTPRequest.new()
	add_child(request)
	
	var error = request.request(apiUrl + "/rt?songId=" + str(song_id), [], HTTPClient.METHOD_GET)
	
	if error != OK:
		push_error("Failed to request thumbnail: " + error)
		
	var params = await request.request_completed
	if params[0] != HTTPRequest.RESULT_SUCCESS:
		return
	var img = Image.new()
	img.load_png_from_buffer(params[3])
	sprite.texture = ImageTexture.create_from_image(img)
	

func _on_response(result, response_code, headers, body) -> void:
	if result != HTTPRequest.RESULT_SUCCESS:
		push_error("Request failed with error: " +  "%s" % response_code)
		return
	
	var song_name = ""
	var song_id = 0
	for h in headers:
		if h.begins_with("SongName: "):
			song_name = h.trim_prefix("SongName: ")
		elif h.begins_with("SongId: "):
			song_id = int(h.trim_prefix("SongId: "))
	
	song_received.emit(song_name, song_id, body)

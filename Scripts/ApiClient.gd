class_name ApiClient
extends Node 

signal song_received

const apiUrl = "http://127.0.0.1:5128/api"
static var userId = "user123" #todo

func init() -> void:
	pass #todo: save/load userid from file

func rate_song(songId: int, positive: bool):
	var request = HTTPRequest.new()
	add_child(request)
	
	var body = JSON.stringify({"songId": songId, "positive" : positive, "userId" : userId})
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
		
func _on_response(result, response_code, headers, body) -> void:
	song_received.emit(result, response_code, headers, body)

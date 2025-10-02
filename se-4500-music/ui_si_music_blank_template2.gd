extends Sprite2D
@onready var http = $HTTPRequest  # Make sure your HTTPRequest node is named exactly "HTTPRequest"


# -------------------- BUTTON SIGNALS --------------------

func _on_x_button_pressed() -> void:
	send_request("http://127.0.0.1:5000/play")       # Skip button → play next song

func _on_replay_button_pressed() -> void:
	send_request("http://127.0.0.1:5000/replay")     # Replay → resume current song

func _on_like_button_pressed() -> void:
	send_request("http://127.0.0.1:5000/like_skip")  # Like → add current song to playlist and skip

func _on_yourlist_button_pressed() -> void:
	send_request("http://127.0.0.1:5000/status")     # YourLists → get current song and playlist info

func _on_home_button_pressed() -> void:
	send_request("http://127.0.0.1:5000/stop")       # Home → stop playback

# -------------------- HELPER FUNCTION --------------------
func send_request(url: String) -> void:
	var err = http.request(url)
	if err != OK:
		print("Failed to send request to ", url)
	else:
		print("Request sent to ", url)

# Optional: handle responses from the server
func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	print("Response code: ", response_code)
	print("Body: ", body.get_string_from_utf8())


func _on_http_request_request_completed(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray) -> void:
	pass # Replace with function body.

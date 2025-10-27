class_name SongPlayer
extends AudioStreamPlayer

var api_client: ApiClient = null
var name_label: Label = null
var last_position: float = 0
var song_id: int = 0

func _init() -> void:
	pass
	
func _enter_tree() -> void:
	api_client = get_node("ApiClient")
	name_label = get_node("SongNameLabel")
	api_client.song_received.connect(_on_song_received)
	get_after_next_frame()

func get_after_next_frame() -> void:
	await get_tree().process_frame
	_load_next_song()

#buttons
func play_pressed() -> void:
	if playing:
		last_position = get_playback_position()
		stop()
	elif has_stream_playback():
		play(last_position)
	elif stream != null:
		play()

func replay_presssed() -> void:
	print("replay")
	seek(0)
	if !playing:
		play()

func next_pressed() -> void:
	print("next")
	if song_id != 0:
		api_client.rate_song(song_id, false)
	_load_next_song()
	
func like_pressed() -> void:
	print("like")
	if song_id != 0:
		api_client.rate_song(song_id, true)
	_load_next_song()

func _load_next_song() -> void:
	if playing:
		playing = false
	song_id = 0
	last_position = 0
	name_label.text = "Loading..."
	api_client.get_next_song()

func _on_song_received(name: String, id: int, body: PackedByteArray) -> void:
	print("Song received")
	name_label.text = name
	song_id = id
	print(song_id)
	stream = AudioStreamMP3.load_from_buffer(body)
	play_pressed()

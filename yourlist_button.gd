extends AudioStreamPlayer

var audio_files = [
	"res://Songs/01 Dynamite.mp3",
	"res://Songs/01 Skyfall.mp3",
	"res://Songs/ABBAStars_DancingQueen_457129-01-003_mp3_256k.mp3"
]

var current_index := -1  

func _ready() -> void:
	randomize()  
	play_random_audio()

func _on_yourlist_button_pressed() -> void:
	play_random_audio()

func play_random_audio() -> void:
	var new_index := current_index
	while new_index == current_index and audio_files.size() > 1:
		new_index = randi() % audio_files.size()

	current_index = new_index
	var audio_path = audio_files[current_index]

	var audio_stream = load(audio_path)
	if audio_stream:
		stop() 
		stream = audio_stream
		play()




	

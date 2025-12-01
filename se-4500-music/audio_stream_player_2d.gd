extends AudioStreamPlayer2D

# List of song
var audio_files = [
	"res://Songs/01 Dynamite.mp3",
	"res://Songs/01 Skyfall.mp3",
	"res://Songs/ABBAStars_DancingQueen_457129-01-003_mp3_256k.mp3"
]

var current_index: int = -1

func _ready() -> void:
	randomize()
	play_random_audio()

	var button = get_node_or_null("../YourListButton")
	if button == null:
		print("❌ Bottone NON trovato! Controlla nome e percorso nel tree!")
	else:
		button.pressed.connect(_on_yourlist_button_pressed)

func _on_yourlist_button_pressed() -> void:
	print("🔘 Bottone premuto!")
	play_random_audio()

func play_random_audio() -> void:
	if audio_files.is_empty():
		print("⚠️ Nessun file audio trovato!")
		return

	var new_index := current_index
	while audio_files.size() > 1 and new_index == current_index:
		new_index = randi() % audio_files.size()

	current_index = new_index
	var audio_path = audio_files[current_index]
	print("🎵 Riproduco: ", audio_path)

	var audio_stream = load(audio_path)
	if audio_stream is AudioStream:
		stop()
		stream = audio_stream
		play()
	else:
		print("❌ Errore nel caricamento audio: ", audio_path)

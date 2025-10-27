# SE-Music-App-2025-CS4500
[gd_scene load_steps=2 format=3 uid="uid://b446rlfgqc66p"]

[ext_resource type="Texture2D" uid="uid://dom0tn7hlvngl" path="res://UI SI Music BLANK TEMPLATE.png" id="1_8vb6a"]

[node name="UiSiMusicBlankTemplate" type="Sprite2D"]
position = Vector2(854.227, 1216)
scale = Vector2(2.92287, 2.92287)
texture = ExtResource("1_8vb6a")

[node name="X button" type="Button" parent="."]
offset_left = -165.0
offset_top = 205.0
offset_right = -39.0
offset_bottom = 333.0
flat = true

[node name="replay button" type="Button" parent="."]
offset_left = -9.65741
offset_top = 205.62
offset_right = 116.343
offset_bottom = 333.62
flat = true

[node name="like button" type="Button" parent="."]
offset_left = 144.985
offset_top = 204.935
offset_right = 270.985
offset_bottom = 332.935
flat = true

[node name="yourlist button" type="Button" parent="."]
offset_left = 217.174
offset_top = -359.236
offset_right = 275.174
offset_bottom = -301.236
flat = true
var audio_file = [
	"res://Song/01 Dynamite.mp3",
	"res://Song/01 Skyfall.mp3",
	"res://Songs/ABBAStars_DancingQueen_457129-01-003_mp3_256k.mp3"
]
func_ready():
	play_random_audio()
	
func play_random_audio():
	var random_index = randi() % audio_files.size()
	var audio_path = audio_files[random_index]
	
	var audio_stream = load(audio_path)
	if audio_stream:
		stream=audio_stream
		play()
	else:
		print("error in the loading of the song: ", audio_path)
	



[node name="home button" type="Button" parent="."]
offset_left = -170.116
offset_top = -359.236
offset_right = -112.116
offset_bottom = -301.236
flat = true

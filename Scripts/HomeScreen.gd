extends Sprite2D

func play_presssed() -> void:
	UIHelper.switch_to_player(self)

func list_presssed() -> void:
	UIHelper.switch_to_list(self)

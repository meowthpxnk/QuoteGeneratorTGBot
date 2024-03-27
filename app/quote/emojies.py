class EmojiManager:
    def __init__(self, emojies_dict: dict):
        self.emojies_dict = emojies_dict

    def __call__(self, emoji_name: str) -> str:
        try:
            return self.emojies_dict[emoji_name]
        except:
            return self.emojies_dict["random"]
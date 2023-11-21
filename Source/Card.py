class Card:
    _id_counter = 0  # Class-level variable to track card IDs

    def __init__(self, title, subtitle, text, value, attack_value, range_value, defense_value, speed_value, layout_url, artwork_url):
        self._card_id = Card._id_counter
        self._title = title
        self._subtitle = subtitle
        self._text = text
        self._value = int(value)
        self._attack_value = int(attack_value)
        self._range_value = int(range_value)
        self._defense_value = int(defense_value)
        self._speed_value = int(speed_value)
        self._layout_url = layout_url
        self._artwork_url = artwork_url

        Card._id_counter += 1

    # Getters
    def get_card_id(self):
        return self._card_id

    def get_title(self):
        return self._title

    def get_subtitle(self):
        return self._subtitle

    def get_text(self):
        return self._text

    def get_value(self):
        return self._value

    def get_attack_value(self):
        return self._attack_value

    def get_range_value(self):
        return self._range_value

    def get_defense_value(self):
        return self._defense_value

    def get_speed_value(self):
        return self._speed_value

    def get_layout_url(self):
        return self._layout_url

    def get_artwork_url(self):
        return self._artwork_url

    # Setters
    def set_card_id(self, card_id):
        self._card_id = card_id

    def set_title(self, title):
        self._title = title

    def set_subtitle(self, subtitle):
        self._subtitle = subtitle

    def set_text(self, text):
        self._text = text

    def set_value(self, value):
        self._value = value

    def set_attack_value(self, attack_value):
        self._attack_value = attack_value

    def set_range_value(self, range_value):
        self._range_value = range_value

    def set_defense_value(self, defense_value):
        self._defense_value = defense_value

    def set_speed_value(self, speed_value):
        self._speed_value = speed_value

    def set_layout_url(self, layout_url):
        self._layout_url = layout_url

    def set_artwork_url(self, artwork_url):
        self._artwork_url = artwork_url

    def __str__(self):
        return f"Card ID: {self._card_id}\nTitle: {self._title}\nSubtitle: {self._subtitle}\nText: {self._text}\nValue: {self._value}\nAttack Value: {self._attack_value}\nRange Value: {self._range_value}\nDefense Value: {self._defense_value}\nSpeed Value: {self._speed_value}\nLayout URL: {self._layout_url}\nArtwork URL: {self._artwork_url}"

    def print_card(self):
        print(f"Card ID: {self.get_card_id()}")
        print(f"Title: {self.get_title()}")
        print(f"Subtitle: {self.get_subtitle()}")
        print(f"Text: {self.get_text()}")
        print(f"Value: {self.get_value()}")
        print(f"Attack Value: {self.get_attack_value()}")
        print(f"Range Value: {self.get_range_value()}")
        print(f"Defense Value: {self.get_defense_value()}")
        print(f"Speed Value: {self.get_speed_value()}")
        print(f"Layout URL: {self.get_layout_url()}")
        print(f"Artwork URL: {self.get_artwork_url()}")

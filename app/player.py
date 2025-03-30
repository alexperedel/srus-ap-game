class Player:
    """Represents a player with a unique ID and name."""

    def __init__(self, unique_id: str, player_name: str):
        self._unique_id = unique_id
        self._player_name = player_name

    def __eq__(self, other):
        if isinstance(other, Player) and self.uid == other.uid:
            return True
        return False

    @classmethod
    def mid_square_hashing(cls, key: str) -> int:
        min_extraction_size = 5
        squared_key = str(int(key) ** 2)
        if len(squared_key) >= min_extraction_size:
            middle = len(squared_key)//2
            middle_digits = squared_key[middle-1:middle+2]
            return int(middle_digits)
        else:
            return int(squared_key)

    def __hash__(self):
        return self.mid_square_hashing(self.uid)

    @property
    def uid(self):
        return self._unique_id

    @property
    def name(self):
        return self._player_name

    @name.setter
    def name(self, name):
        self._player_name = name

    def __str__(self):
        return f"Player {self._player_name} (ID: {self._unique_id})"

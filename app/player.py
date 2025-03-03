class Player:
    """Represents a player with a unique ID and name."""

    def __init__(self, unique_id: str, player_name: str):
        self._unique_id = unique_id
        self._player_name = player_name

    @property
    def uid(self):
        return self._unique_id

    @property
    def name(self):
        return self._player_name

    def __str__(self):
        return f"Player {self._player_name} (ID: {self._unique_id})"

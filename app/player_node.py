class PlayerNode:
    """Represents a node in a doubly linked list containing a Player object."""

    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        next_id = self.next.key if self.next else "None"
        previous_id = self.previous.key if self.previous else "None"
        return f"Player id: {self.key}, next {next_id}, previous {previous_id}"

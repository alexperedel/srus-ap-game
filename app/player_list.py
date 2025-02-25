from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        if self._head is None:
            return True

        return False

    def append(self, player):
        if self.is_empty():
            self._head, self._tail = PlayerNode(player)

        else:
            player_node = PlayerNode(player)
            



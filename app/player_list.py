from app.player_node import PlayerNode


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
            node = PlayerNode(player)
            self._head = node
            self._tail = node
        else:
            player_node = PlayerNode(player)
            player_node.next = self._head
            self.head.previous = player_node
            self._head = player_node
            



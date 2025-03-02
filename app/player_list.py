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

    def _add_first_node(self, node):
        self._head = node
        self._tail = node

    def append_left(self, player):
        if self.is_empty():
            self._add_first_node(PlayerNode(player))
        else:
            player_node = PlayerNode(player)
            player_node.next = self._head
            self.head.previous = player_node
            self._head = player_node

    def append_right(self, player):
        if self.is_empty():
            self._add_first_node(PlayerNode(player))
        else:
            player_node = PlayerNode(player)
            player_node.previous = self._tail
            self.tail.next = player_node
            self._tail = player_node
            



from app.player_node import PlayerNode
from app.exceptions import DeletionFromEmptyList


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

    def delete_head(self):
        if self.is_empty():
            raise DeletionFromEmptyList()

        if self._head.next is not None:
            next_node = self._head.next
            next_node.previous = None
            self._head = next_node
        else:
            self._head = None
            self._tail = None

    def delete_tail(self):
        if self.is_empty():
            raise DeletionFromEmptyList()

        if self._tail.previous is not None:
            previous_node = self._tail.previous
            previous_node.next = None
            self._tail = previous_node
        else:
            self._head = None
            self._tail = None
            



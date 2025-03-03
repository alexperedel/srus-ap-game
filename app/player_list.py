from app.player_node import PlayerNode
from app.exceptions import DeletionFromEmptyList


class PlayerList:

    """A linked list-like structure to manage players.

    This class maintains a head and tail reference for managing a list of players.
    """

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

        """Adds a player to the beginning (head) of the list.

        Args:
            player (object): The player object to be added.
        """

        if self.is_empty():
            self._add_first_node(PlayerNode(player))
        else:
            player_node = PlayerNode(player)
            player_node.next = self._head
            self.head.previous = player_node
            self._head = player_node

    def append_right(self, player):

        """Adds a player to the end (tail) of the list.

        Args:
            player (object): The player object to be added.
        """

        if self.is_empty():
            self._add_first_node(PlayerNode(player))
        else:
            player_node = PlayerNode(player)
            player_node.previous = self._tail
            self.tail.next = player_node
            self._tail = player_node

    def delete_head(self):

        """Removes the first player from the list.

        Raises:
            DeletionFromEmptyList: If the list is empty.
        """

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

        """Removes the last player from the list.

        Raises:
            DeletionFromEmptyList: If the list is empty.
        """

        if self.is_empty():
            raise DeletionFromEmptyList()

        if self._tail.previous is not None:
            previous_node = self._tail.previous
            previous_node.next = None
            self._tail = previous_node
        else:
            self._head = None
            self._tail = None

    def delete_by_key(self, key):

        """Deletes a player from the list based on a given key.

        Args:
            key (str or int): The key identifying the player to be removed.

        Raises:
            DeletionFromEmptyList: If the list is empty.

        Returns:
            str: A message if the key is not found.
        """

        if self.is_empty():
            raise DeletionFromEmptyList()

        current_node = self._head

        while current_node is not None:
            if str(current_node.key) == str(key):
                if current_node.previous is None and current_node.next is None:
                    self._head = None
                    self._tail = None
                elif current_node.previous is None:
                    self.delete_head()
                elif current_node.next is None:
                    self.delete_tail()
                else:
                    next_node = current_node.next
                    previous_node = current_node.previous
                    previous_node.next = next_node
                    next_node.previous = previous_node
                return
            else:
                current_node = current_node.next
        else:
            return f"No item with key: {key} was found"

    def display(self, forward=True):

        """Displays the list of players in forward or backward order.

            Args:
                forward (bool, optional): If True, displays from head to tail;
                                          if False, displays from tail to head. Defaults to True.
            """

        if self.is_empty():
            print("List is Empty!")
            return

        if forward:
            current_node = self._head
            while current_node is not None:
                print(str(current_node))
                current_node = current_node.next
        else:
            current_node = self._tail
            while current_node is not None:
                print(current_node)
                current_node = current_node.previous


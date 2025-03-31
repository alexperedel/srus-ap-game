from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:

    """
    A class representing a hash map for storing players, where each player is associated with a unique key.
    This implementation uses chaining (linked lists) to resolve hash collisions.
    """

    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(10)]

    def _get_index(self, key: str | Player) -> int:

        """
        Computes the index in the hash map for a given key, either a string or a Player object.

        Args:
            key (str | Player): The key for the hash map. Can either be a string or a Player object.

        Returns:
            int: The index corresponding to the hash value of the key.
        """

        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.mid_square_hashing(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:

        """
        Sets the player in the hash map by key. If the player already exists, their name is updated.
        If the player does not exist, a new Player is created and added to the linked list.

        Args:
            key (str): The key (ID) for the player.
            name (str): The name of the player to be associated with the key.
        """

        player_list = self.hashmap[self._get_index(key)]
        if not player_list.is_empty():
            player = player_list.find_by_key(key)
            if player:
                player.name = name
            else:
                new_player = Player(key, name)
                player_list.append_right(new_player)
        else:
            new_player = Player(key, name)
            player_list.append_right(new_player)

    def __getitem__(self, key: str) -> Player | None:

        """
        Retrieves the player associated with the given key.

        Args:
            key (str): The key (ID) for the player.

        Returns:
            Player | None: The player associated with the key, or None if not found.
        """

        player_list = self.hashmap[self._get_index(key)]

        if not player_list.is_empty():
            player = player_list.find_by_key(key)
            if player:
                return player
        return

    def __len__(self) -> int:
        counter = 0
        for item in self.hashmap:
            counter += len(item)
        return counter

    def __delitem__(self, key: str) -> None:

        """
        Deletes the player associated with the given key.

        Args:
            key (str): The key (ID) for the player to be deleted.

        Returns:
            None
        """

        linked_list = self.hashmap[self._get_index(key)]
        if not linked_list.is_empty():
            player = linked_list.find_by_key(key)
            if player:
                del self.hashmap[self._get_index(key)]

    def display(self):
        for index, item in enumerate(self.hashmap):
            print(f"Key: {index}")
            if hasattr(item, "display"):
                item.display()




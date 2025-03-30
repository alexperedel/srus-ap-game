from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(10)]

    def _get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.mid_square_hashing(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
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

    def __delitem__(self, key: str) -> None | str:
        linked_list = self.hashmap[self._get_index(key)]
        if not linked_list.is_empty():
            player = linked_list.find_by_key(key)
            if player:
                del self.hashmap[self._get_index(key)]
            else:
                return "Player was not found!"

    def display(self):
        for index, item in enumerate(self.hashmap):
            print(f"Key: {index}")
            if hasattr(item, "display"):
                item.display()




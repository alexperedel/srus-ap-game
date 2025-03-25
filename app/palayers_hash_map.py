from player_list import PlayerList
from player import Player


class PlayerHashMap:
    SIZE: int = 10

    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(10)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.mid_square_hashing(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
        player_list = self.hashmap[self.get_index(key)]
        if not player_list.is_empty():
            player = player_list.find_by_key(key)
            if player:
                player.player.name = name
            else:
                new_player = Player(key, name)
                player_list.append_right(new_player)

    def __getitem__(self, key: str) -> Player | None:
        player_list = self.hashmap[self.get_index(key)]

        if not player_list.is_empty():
            player = player_list.find_by_key(key)
            if player:
                return player.player
        return


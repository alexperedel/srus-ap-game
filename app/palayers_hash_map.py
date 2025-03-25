from player_list import PlayerList
from player import Player

class PlayerHashMap:
    SIZE: int = 10
    def __init__(self):
        self.hashmap = [PlayerList() for _ in range(10)]

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE  # TODO: implement __hash__ in player
        else:
            return Player.__hash__(key) % self.SIZE  # TODO implement a hash class method in Player

    # def __setitem__(self, key: str, name: str) -> none:
    #     """ Psuedo code:
    #     1. Use the key to calculate an index into the hash map
    #        (TODO: Implement a hash function in the Player class that returns a player hash and then modulate it by the size of the hashmap)
    #     2. Get the PlayerList at that index
    #     3. Check if the player is already on that player list.
    #          If it is, update the player's name.
    #          If it isn't, create a player and add the player to the player list.
    #
    #      """
    #     # get the player's appropriate PlayerList:
    #     player_list = self.hashmap[self.get_index(key)]
    #     # check if the player is in the list
    #     # If it is, update the player's name
    #     # If it isn't, create a player and add the player to the player list
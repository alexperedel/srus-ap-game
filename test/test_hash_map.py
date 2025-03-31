import unittest

from app.players_hash_map import PlayerHashMap
from app.player import Player


class TestPlayerHashMap(unittest.TestCase):

    def test_successfully_set_items_with_collisions(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")
        player_2 = Player("80000", "Julia")

        player_hash_map = PlayerHashMap()

        player_hash_map[player.uid] = player.name
        player_hash_map[player_1.uid] = player_1.name
        player_hash_map[player_2.uid] = player_2.name
        player_hash_map[player.uid] = "Drake"

        self.assertEqual(player_hash_map[player.uid].name, "Drake")
        self.assertEqual(player_hash_map[player_1.uid].name, "Tom")
        self.assertEqual(player_hash_map[player_2.uid].name, "Julia")

    def test_successfully_set_items_no_collisions(self):
        player = Player("12345", "John")
        player_1 = Player("54321", "Tom")
        player_2 = Player("58", "Julia")

        player_hash_map = PlayerHashMap()

        player_hash_map[player.uid] = player.name
        player_hash_map[player_1.uid] = player_1.name
        player_hash_map[player_2.uid] = player_2.name
        player_hash_map[player.uid] = "Drake"

        self.assertEqual(player_hash_map[player.uid].name, "Drake")
        self.assertEqual(player_hash_map[player_1.uid].name, "Tom")
        self.assertEqual(player_hash_map[player_2.uid].name, "Julia")

    def test_successfully_get_items(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")
        player_2 = Player("80000", "Julia")
        player_3 = Player("10000", "Sandy")

        player_hash_map = PlayerHashMap()

        player_hash_map[player.uid] = player.name
        player_hash_map[player_1.uid] = player_1.name
        player_hash_map[player_2.uid] = player_2.name

        result = player_hash_map[player.uid]
        result_1 = player_hash_map[player_1.uid]
        result_2 = player_hash_map[player_2.uid]
        result_3_empty = player_hash_map[player_3.uid]

        self.assertEqual(result, player)
        self.assertEqual(result_1, player_1)
        self.assertEqual(result_2, player_2)
        self.assertIsNone(result_3_empty)

    def test_successfully_get_len_of_hashmap(self):
        player = Player("12345", "John")
        player_1 = Player("54321", "Tom")
        player_2 = Player("58", "Julia")

        player_hash_map = PlayerHashMap()

        player_hash_map[player.uid] = player.name
        player_hash_map[player_1.uid] = player_1.name
        player_hash_map[player_2.uid] = player_2.name

        result = len(player_hash_map)

        self.assertEqual(result, 3)

    def test_successfully_delete_item(self):
        player = Player("12345", "John")
        player_1 = Player("54321", "Tom")
        player_2 = Player("58", "Julia")

        player_hash_map = PlayerHashMap()

        player_hash_map[player.uid] = player.name
        player_hash_map[player_1.uid] = player_1.name
        player_hash_map[player_2.uid] = player_2.name

        del player_hash_map[player.uid]

        result = len(player_hash_map)

        self.assertEqual(result, 2)

    def test_delete_item_empty_table(self):
        player_hash_map = PlayerHashMap()

        del player_hash_map["10000"]

        result = len(player_hash_map)

        self.assertEqual(result, 0)

    def test_delete_non_existent_item(self):
        player_hash_map = PlayerHashMap()

        player = Player("20000", "John")
        player_hash_map[player.uid] = player.name

        del player_hash_map["10000"]

        result = len(player_hash_map)

        self.assertEqual(result, 1)

    def test_successfully_get_key_index(self):
        player_hash_map = PlayerHashMap()

        player = Player("58", "Julia")
        player_1 = Player("20000", "John")
        key = "3"

        result = player_hash_map._get_index(player)
        result_1 = player_hash_map._get_index(player_1)
        result_2 = player_hash_map._get_index(key)

        self.assertEqual(result, 4)
        self.assertEqual(result_1, 0)
        self.assertEqual(result_2, 9)




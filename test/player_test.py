import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def test_successfully_get_player_unique_id(self):
        player = Player("20000", "John")
        player_unique_id = player.uid
        self.assertEqual(player_unique_id, "20000")

    def test_successfully_get_player_name(self):
        player = Player("20000", "John")
        player_unique_id = player.name
        self.assertEqual(player_unique_id, "John")

    def test_successfully_get_hash_id_len_more_than_five(self):
        player = Player("12345", "John")
        hash_value = hash(player)
        self.assertEqual(hash_value, 399)

    def test_successfully_get_hash_id_len_less_than_five(self):
        player = Player("5", "John")
        hash_value = hash(player)
        self.assertEqual(hash_value, 25)

import unittest

from app.player_list import PlayerList
from app.player import Player


class TestPlayerList(unittest.TestCase):
    def test_successfully_append_left_player_empty_list(self):
        player = Player("20000", "John")
        player_list = PlayerList()

        player_list.append_left(player)

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.key, player.uid)
        self.assertEqual(head, tail)

    def test_successfully_append_left_player_not_empty_list(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")

        player_list = PlayerList()

        player_list.append_left(player)
        player_list.append_left(player_1)

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.key, player_1.uid)
        self.assertEqual(tail.key, player.uid)
        self.assertEqual(head.next.key, player.uid)
        self.assertEqual(tail.previous.key, player_1.uid)

    def test_successfully_append_right_player_empty_list(self):
        player = Player("20000", "John")
        player_list = PlayerList()

        player_list.append_right(player)

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(tail.key, player.uid)
        self.assertEqual(tail, head)

    def test_successfully_append_right_player_not_empty_list(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")

        player_list = PlayerList()

        player_list.append_right(player)
        player_list.append_right(player_1)

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.key, player.uid)
        self.assertEqual(tail.key, player_1.uid)
        self.assertEqual(head.next.key, player_1.uid)
        self.assertEqual(tail.previous.key, player.uid)



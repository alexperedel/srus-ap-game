import unittest

from app.player_list import PlayerList
from app.player import Player
from app.exceptions import DeletionFromEmptyList


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

    def test_successfully_delete_head_not_empty_list_with_one_node(self):
        player = Player("20000", "John")
        player_list = PlayerList()
        player_list.append_right(player)
        player_list.delete_head()

        head = player_list.head
        tail = player_list.tail

        self.assertIsNone(head)
        self.assertIsNone(tail)

    def test_successfully_delete_tail_not_empty_list_with_one_node(self):
        player = Player("20000", "John")
        player_list = PlayerList()
        player_list.append_right(player)
        player_list.delete_tail()

        head = player_list.head
        tail = player_list.tail

        self.assertIsNone(head)
        self.assertIsNone(tail)

    def test_successfully_delete_head_not_empty_list_with_several_nodes(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")

        player_list = PlayerList()
        player_list.append_left(player)
        player_list.append_left(player_1)
        player_list.delete_head()

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.key, player.uid)
        self.assertEqual(tail.key, player.uid)
        self.assertIsNone(head.previous)

    def test_successfully_delete_tail_not_empty_list_with_several_nodes(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")

        player_list = PlayerList()
        player_list.append_right(player)
        player_list.append_right(player_1)
        player_list.delete_tail()

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.key, player.uid)
        self.assertEqual(tail.key, player.uid)
        self.assertIsNone(tail.next)

    def test_successfully_delete_head_empty_list(self):
        player_list = PlayerList()

        with self.assertRaises(DeletionFromEmptyList) as error:
            player_list.delete_head()

        self.assertEqual(str(error.exception), "Cannot delete from an empty list!")

    def test_successfully_delete_tail_empty_list(self):
        player_list = PlayerList()

        with self.assertRaises(DeletionFromEmptyList) as error:
            player_list.delete_tail()

        self.assertEqual(str(error.exception), "Cannot delete from an empty list!")

    def test_successfully_delete_item_by_key_not_empty_list_with_several_nodes(self):
        player = Player("20000", "John")
        player_1 = Player("50000", "Tom")
        player_2 = Player("80000", "Julia")

        player_list = PlayerList()
        player_list.append_right(player)
        player_list.append_right(player_1)
        player_list.append_right(player_2)
        player_list.delete_by_key("50000")

        head = player_list.head
        tail = player_list.tail

        self.assertEqual(head.next, tail)
        self.assertEqual(tail.previous, head)

    def test_successfully_delete_item_by_key_not_empty_list_with_one_node(self):
        player = Player("20000", "John")
        player_list = PlayerList()
        player_list.append_right(player)
        player_list.delete_by_key("20000")

        head = player_list.head
        tail = player_list.tail

        self.assertIsNone(head)
        self.assertIsNone(tail)

    def test_successfully_delete_item_by_key_empty_list(self):
        player_list = PlayerList()

        with self.assertRaises(DeletionFromEmptyList) as error:
            player_list.delete_by_key("2000")

        self.assertEqual(str(error.exception), "Cannot delete from an empty list!")

    def test_successfully_delete_item_by_key_with_non_existent_key(self):
        player = Player("20000", "John")
        key = "40000"
        player_list = PlayerList()
        player_list.append_right(player)
        result = player_list.delete_by_key(key)

        self.assertEqual(result, f"No item with key: {key} was found")



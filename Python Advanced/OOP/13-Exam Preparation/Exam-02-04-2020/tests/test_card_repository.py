import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.cr = CardRepository()

    def test_set_attr(self):
        self.assertEqual(self.cr.count, 0)
        self.assertEqual(len(self.cr.cards), 0)

    def test_add_raises(self):
        c = MagicCard("test")
        self.cr.add(c)
        with self.assertRaises(ValueError) as ex:
            self.cr.add(c)
        self.assertEqual(str(ex.exception), "Card test already exists!")

    def test_add(self):
        c = MagicCard("test")
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)
        self.assertEqual(len(self.cr.cards), 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cr.remove("")
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_remove(self):
        c = MagicCard("test")
        self.cr.add(c)
        self.assertEqual(self.cr.count, 1)
        self.cr.remove("test")
        self.assertEqual(self.cr.count, 0)

    def test_find(self):
        p = MagicCard("test")
        self.cr.add(p)
        res = self.cr.find("test")
        self.assertEqual(res.name, "test")

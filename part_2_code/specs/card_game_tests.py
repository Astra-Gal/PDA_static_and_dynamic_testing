import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Diamonds", 7)
        self.card3 = Card("Hearts", 3)
        self.cards = []
        self.card_game = CardGame

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self, self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self, self.card2, self.card3))

    def test_cards_total(self):
        cards = [self.card2, self.card3]
        self.assertEqual("You have a total of 10", self.card_game.cards_total(self, cards))
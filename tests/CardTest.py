import unittest
from model import Card


class CardTestCase(unittest.TestCase):

    def test_deck_has_52_cards(self):
        # GIVEN
        suit = 2
        rank = 10

        # WHEN
        my_card = Card(suit, rank)

        # THEN
        self.assertEqual(my_card.get_rank(), rank)
        self.assertEqual(my_card.get_suit(), suit)


if __name__ == '__main__':
    unittest.main()

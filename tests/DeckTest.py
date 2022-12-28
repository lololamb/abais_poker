import unittest
from model import Card
from model import Deck


class DeckTestCase(unittest.TestCase):

    # Le jeu doit contenir 52 cartes
    def test_card_has_rank_and_suit(self):
        # GIVEN
        deck = Deck()

        # WHEN
        deck.initialize()

        # THEN
        self.assertEqual(52, deck.get_length())

    # Le mélange du jeu doit donner un ordre différent
    def test_shuffle_must_result_as_a_different_order(self):
        # GIVEN
        deck_as_reference = Deck()
        deck_to_shuffle = Deck()
        deck_as_reference.initialize()
        deck_to_shuffle.initialize()

        # WHEN
        deck_to_shuffle.shuffle()

        # THEN
        base_order = deck_as_reference.__str__()
        shuffled_order = deck_to_shuffle.__str__()
        self.assertNotEqual(base_order, shuffled_order)

    # Le pop retire la dernière carte
    def test_pop_removes_latest_card(self):
        # GIVEN
        deck = Deck()
        deck.initialize()

        # WHEN
        pop_card = deck.pop()

        # THEN
        print(pop_card)
        self.assertEqual(12, pop_card.get_rank())
        self.assertEqual(3, pop_card.get_suit())
        self.assertEqual(51, deck.get_length())


if __name__ == '__main__':
    unittest.main()

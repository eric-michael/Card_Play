
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Deck:

    def __init__(self, starting_deck):

        self.deck = starting_deck

    def __add_card__(self, card):

        self.deck.append(card)

    def __remove_card__(self, card):

        self.deck.remove(card)

    def __repr__(self):

        return self.deck



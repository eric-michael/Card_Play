import random


class Game:

    def __init__(self, deck):

        self.deck = deck.deck

        self.draw_count = 5

        self.max_card_limit = 8

        self.draw_pile = []

        self.discard_pile = []

        self.hand = []

    def start_game(self):

        for x in self.deck:
            self.draw_pile.append(x)

        random.shuffle(self.draw_pile)

        for x in range(0, self.draw_count):
            self.hand.append(self.draw_pile.pop())

    def end_game(self):

        self.draw_pile.clear()
        self.discard_pile.clear()
        self.hand.clear()

    def view_hand(self):

        return self.hand

    def view_draw_pile(self):

        return self.draw_pile

    def view_discard_pile(self):

        return self.discard_pile

    def draw_card(self):

        if len(self.hand) >= self.max_card_limit:
            return 'You can\'t draw any more cards'

        # If there are cards in the draw pile, add a card to your hand
        if self.draw_pile:

            card = self.draw_pile.pop()
            self.hand.append(card)
            return "You drew " + card

        # If there are no cards in the draw pile, shuffle the discard pile into the draw pile
        # Then, draw a card
        elif self.discard_pile:

            while self.discard_pile:

                self.draw_pile.append(self.discard_pile.pop())

            if self.draw_pile:

                card = self.draw_pile.pop()
                self.hand.append(card)
                return "You drew " + card
        else:
            return "There are no cards to draw!"

    # I can change this one one line with pop()
    def play_card(self, card):

        if self.hand.count(card):

            self.discard_pile.append(card)
            self.hand.remove(card)
            return 'You played ' + card
        else:
            return 'Invalid card choice'

    def empty_hand(self):
        for x in range(len(self.hand)):
            self.discard_pile.append(self.hand.pop())

    def add_card_to_deck(self, card):

        self.deck.append(card)

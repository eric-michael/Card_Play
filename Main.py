import Deck
import Match

# TODO
#  Create logic to have a "start game" option and an "end application" option.


print("Welcome to Card Play\n\n")

deck = Deck.Deck(Deck.deck)

game = Match.Game(deck)

game.start_game()

selection = 0

while selection != 5:

    print("Hand: ")
    print(game.view_hand())

    selection = input("1. Draw a card\n"
                      "2. Play a card\n"
                      "3. End Turn\n"
                      "4. View Draw Pile\n"
                      "5. View Discard Pile\n"
                      "6. End Game\n")

    if selection == '1':
        card = game.draw_card()
        print(card)
    elif selection == '2':
        print(game.view_hand())
        card = input("\nSelect a card to play\n")
        print(game.play_card(card))
        print(game.view_hand())
    elif selection == '3':
        game.empty_hand()
    elif selection == '4':
        print(game.view_draw_pile())
    elif selection == '5':
        print(game.view_discard_pile())
    elif selection == '6':
        game.end_game()
    else:
        selection = input("Please enter one of the above selections\n")


# Author: <Your name>
# Assignment #3 - Blackjack
# Date due: 2021-10-28
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########


def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card"""
    the_card = random.randint(1, 13)
    if the_card == 1:
        return "A"
    elif the_card == 11:
        return "J"
    elif the_card == 12:
        return "Q"
    elif the_card == 13:
        return "K"
    else:
        return str(the_card)


def get_card_value(card_label):
    """Evaluates to the integer value associated with
        the card label (a single- or double-character string)
        :param card_label: a single- or double-character string representing a card
        :return: an int representing the card's value"""
    if card_label.isdigit():
        return int(card_label)
    elif card_label == "A":
        return 1
    elif card_label == "J" or card_label == "Q" or card_label == "K":
        return 10


def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    card_one = deal_card()
    card_two = deal_card()
    player_total = get_card_value(card_one) + get_card_value(card_two)

    print("Player drew {} and {}.".format(card_one, card_two))
    print("Player's total is {}.".format(player_total))
    print("")

    options = input("Hit (h) or Stay (s)? ")

    while options != "s" and player_total < BLACKJACK:
        while options == "h" and player_total < BLACKJACK:
            addtional_card = deal_card()
            player_total += get_card_value(addtional_card)
            print()
            print("Player drew {}.".format(addtional_card))
            print("Player's total is {}.".format(player_total))
            print()
            if player_total < BLACKJACK:
                options = input("Hit (h) or Stay (s)? ")
        while options != "h" and options != "s":
            print()
            options = input("Hit (h) or Stay (s)? ")
    if options == "s":
        print()
    return player_total


def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total
    :return: the total value of the cards dealt
    """
    card_one = deal_card()
    card_two = deal_card()
    dealer_total = get_card_value(card_one) + get_card_value(card_two)

    print("The dealer has {} and {}.".format(card_one, card_two))
    print("Dealer's total is {}.".format(dealer_total))
    print("")

    while dealer_total <= DEALER_THRESHOLD:
        addtional_card = deal_card()
        dealer_total += get_card_value(addtional_card)
        print("Dealer drew {}.".format(addtional_card))
        print("Dealer's total is {}.".format(dealer_total))
        print()

    return dealer_total


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """
    if player_total > dealer_total and player_total <= 21 :
        print("YOU WIN!")
        print()
    elif dealer_total >= 21 and player_total <= 21:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
        print()


def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome
    :return: None
    """
    print("Let's Play Blackjack!")
    print()
    play_again_option = "Y"
    while play_again_option !="N":
        players_outcome=deal_cards_to_player()
        if players_outcome > 21:
            print("YOU LOSE!")
            print()
        elif players_outcome == 21:
            dealer_outcome=deal_cards_to_dealer()
            if dealer_outcome==21:
                print("YOU LOSE!")
                print()
            else:
                print("YOU WIN!")
                print()
        else:
            dealer_outcome = deal_cards_to_dealer()
            if dealer_outcome > 21:
                print("YOU WIN!")
                print()
            else:
                determine_outcome(players_outcome, dealer_outcome)
        play_again_option=input("Play again (Y/N)? ")
        if play_again_option=="Y":
            print()
        while play_again_option !="Y" and play_again_option !="N":
            print()
            play_again_option = input("Play again (Y/N)? ")
    print()
    print("Goodbye.")


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """
    play_blackjack()
    # call play_blackjack() here and remove pass below


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()

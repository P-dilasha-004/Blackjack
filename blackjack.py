from random import randint

num_players = int(input("Welcome to Blackjack! How many players? "))
players = []
score = {}
for i in range(1, num_players+1):
    name = input("What is player " + str(i)+"'s name? ")
    players.append(name)
    score[name] = 3

def print_card_name(card_rank):
    if card_rank == 1:
        card_name = 'Ace'
    elif card_rank == 11:
        card_name = 'Jack'
    elif card_rank == 12:
        card_name = 'Queen'
    elif card_rank == 13:
        card_name = 'King'
    else:
        card_name = card_rank

    if card_rank == 8 or card_rank == 1:
        print('Drew an ' + str(card_name))
    elif card_rank < 1 or card_rank > 13:
        print('BAD CARD')
    else:
        print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
#
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.


def draw_card():
    card_rank = randint(1, 13)
    print_card_name(card_rank)

    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank

    return card_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
#
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none


def print_header(message):
    print('-----------')
    print(message)
    print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
#
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.


def draw_starting_hand(name):
    print_header(name+"'s TURN")
    return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
#
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none


def print_end_turn_status(hand_value):
    print('Final hand: ' + str(hand_value) + '.')

    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')


# Prints the end game banner and the winner based on the final hands.
#
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none

def print_end_game_status(user_hand, dealer_hand, record):
    print_header('GAME RESULT')

    for player, player_hand in record.items():
        if player_hand <= 21 and (player_hand > dealer_hand or dealer_hand > 21):
            score[player] += 1
            print(f'{player} wins! Score: {score[player]}')

        elif player_hand > 21 or (dealer_hand <= 21 and dealer_hand > player_hand):
            score[player] -= 1
            print(f'{player} loses! Score: {score[player]}')

        else:
            print(f'{player} pushes. Score: {score[player]}')
        if score[player] == 0:
          print(f'{player} eliminated!')
          players.remove(player)
        
# USER'S TURN

should_continue = ""

while should_continue != "n":
    record = {}
    for player in players:
        user_hand = draw_starting_hand(player)
        should_hit = 'y'
        while user_hand < 21:
            should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
            if should_hit == 'n':
                break
            elif should_hit != 'y':
                print("Sorry I didn't get that.")
            else:
                user_hand = user_hand + draw_card()
        print_end_turn_status(user_hand)
        record[player] = user_hand

    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
        print("Dealer has {}.".format(dealer_hand))
        dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)

    # GAME RESULT
    print_end_game_status(user_hand, dealer_hand, record)
    should_continue = input("Do you want to play another hand (y/n)? ")
    if should_continue == "n":
        print("Thank you for playing the Blackjack Game!")
        break

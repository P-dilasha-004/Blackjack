# Blackjack Game in Python 

This project is a simple Blackjack game built using Python.

# Features
+ **Interactive gameplay:** Users can play against a dealer. Users can play multiple hands in a single game. 
+ **Card drawing:** Cards are drawn randomly for each player and dealer.
+ **User decisions:** Players can choose to "Hit" (draw a card) by choosing "y or Y" or "Stand" (keep current hand) by choosing "n or N".
+ **Game results:** The game determines the winner based on the final hand values of players against the dealer.

# How to Play
+ **Start the game:** Run the Python script to begin the game.
+ **Enter player information:** Specify the number of players and input player names.
+ **Gameplay:** Each player takes turns drawing cards and deciding whether to "Hit" or "Stand".
After each draw, the player's hand value will be displayed. 
Players can continue to "Hit" until they choose to "Stand" or their hand value exceeds 21.
+ **Dealer's turn:** The dealer draws cards and reveals their final hand.
+ **Game result:** The game compares each player's final hand with the dealer's, and the winner is determined.

# Card Values
+ Number cards are worth their face value (2-10).
+ Face cards (J, Q, K) are worth 10.
+ Aces are worth 11. 

## Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/Blackjack.git
cd Blackjack
```
Run the game:
```bash
python blackjack.py
```

# How to Play
+ **Start the game:** Run the Python script to initiate the game.
+ **Enter players' names:** The game will prompt for the number of players and their names.
+ **Hit or Stand:** Players will be asked whether they want to "Hit" or "Stand" after each card draw.
+ **Final Hands:** After all players finish their turn, the dealer will play according to set rules (e.g., hit until the hand is 17 or higher).
+ **Game Results:** After the dealer's turn, the game will announce the winners and losers.
  
# Game Rules
+ **Goal:** The aim of the game is to have a hand value as close to 21 as possible without exceeding it.
   + Players' Actions:
          Hit (Draw a card) OR 
          Stand (Keep current hand and end your turn)
   + Dealer's Actions:
          The dealer automatically "Hits" until their hand value is 17 or higher.
+ **Scoring:** Each player starts with a score of 3, and their score is updated based on the outcome of each round.

# Example Gameplay 
```text
Welcome to Blackjack! How many players? 2
What is player 1's name? Player 1 
What is player 2's name? Player 2
-----------
Player 1's TURN
-----------
Drew a 5
Drew a 7
You have 12. Hit (y/n)? y
Drew a Queen
Final hand: 22.
BUST.
-----------
Player 2's TURN
-----------
Drew a Jack
Drew a 6
You have 16. Hit (y/n)? n
Final hand: 16.
-----------
DEALER's TURN
-----------
Drew a 9
Drew a 4
Dealer has 13.
Drew an 8
Final hand: 21.
BLACKJACK!
-----------
GAME RESULT
-----------
Player 1 loses! Score: 2
Player 2 loses! Score: 2
Do you want to play another hand (y/n)? y
-----------
Player 1's TURN
-----------
Drew a 4
Drew a 5
You have 9. Hit (y/n)? y
Drew a 3
You have 12. Hit (y/n)? y
Drew an 8
You have 20. Hit (y/n)? n
Final hand: 20.
-----------
Player 2's TURN
-----------
Drew a 5
Drew a King
You have 15. Hit (y/n)? y
Drew an 8
Final hand: 23.
BUST.
-----------
DEALER's TURN
-----------
Drew an Ace
Drew an Ace
Final hand: 22.
BUST.
-----------
GAME RESULT
-----------
Player 1 wins! Score: 3
Player 2 loses! Score: 1
Do you want to play another hand (y/n)? n
Thank you for playing the Blackjack Game!
```

# Contributing
Contributions are welcome! Here's how you can help:

+ Fork the repository.
+ Create a new feature branch (git checkout -b feature-branch).
+ Commit your changes (git commit -m 'Add feature').
+ Push to the branch (git push origin feature-branch).
+ Create a new Pull Request.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/P-dilasha-004/Blackjack/blob/main/LICENSE)
 file for details.

# Additional Notes
This game is a personal project for learning Python. 
You can modify the deck of cards or add additional game features as desired.

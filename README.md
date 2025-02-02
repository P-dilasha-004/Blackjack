# Blackjack Game in Python 

This project is a simple Blackjack game built using Python.

# Features
+ **Interactive gameplay:** Users can play with multiple players and against a dealer.
+ **Card drawing:** Cards are drawn randomly for each player and dealer.
+ **User decisions:** Players can choose to "Hit" (draw a card) or "Stand" (keep current hand).
+ **Game results:** The game determines the winner based on the final hand values.

# How to Play
+ **Start the game:** Run the Python script to begin the game.
+ **Enter player information:** Specify the number of players and input player names.
+ **Gameplay:** Each player takes turns drawing cards and deciding whether to "Hit" or "Stand".
After each draw, the player's hand value will be displayed. 
Players can continue to "Hit" until they choose to "Stand" or their hand value exceeds 21.
+ **Dealer's turn:** The dealer draws cards based on predefined rules and reveals their final hand.
+ **Game result:** The game compares each player's final hand with the dealer's, and the winner is determined.

# Card Values
+ Number cards are worth their face value (2-10).
+ Face cards (J, Q, K) are worth 10.
+ Aces can be worth either 1 or 11, depending on the player's hand.

# Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/blackjack-game.git
cd blackjack-game
Run the game:

bash
Copy
Edit
python blackjack.py
# How to Play
Start the game: Run the Python script to initiate the game.
Enter players' names: The game will prompt for the number of players and their names.
Hit or Stand: Players will be asked whether they want to "Hit" or "Stand" after each card draw.
Final Hands: After all players finish their turn, the dealer will play according to set rules (e.g., hit until the hand is 17 or higher).
Game Results: After the dealer's turn, the game will announce the winners and losers.
Game Rules
Goal: The aim of the game is to have a hand value as close to 21 as possible without exceeding it.
Players' Actions:
Hit: Draw a card.
Stand: Keep current hand and end your turn.
Dealer's Actions: The dealer must "Hit" until their hand value is 17 or higher.
Scoring: Each player starts with a score of 3, and their score is updated based on the outcome of each round.

# Project Structure
```python
├── blackjack
     ├── blackjack.py           # Main game script
     ├── README.md              # Project documentation
```

# Contributing
Contributions are welcome! Here's how you can help:

+ Fork the repository.
+ Create a new feature branch (git checkout -b feature-branch).
+ Commit your changes (git commit -m 'Add feature').
+ Push to the branch (git push origin feature-branch).
+ Create a new Pull Request.

# License
This project is licensed under the MIT License - see the [Github][https://github.com/P-dilasha-004/Blackjack/blob/main/LICENSE] file for details.

# Additional Notes
This game is a personal project for learning Python. 
You can modify the deck of cards or add additional game rules as desired.

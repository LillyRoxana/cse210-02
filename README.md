## cse210-02

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.


## Synopsis

The player starts the game with 300 points. Individual cards are represented as a number from 1 to 13.
The current card is displayed. The player guesses if the next one will be higher or lower.
The the next card is displayed. The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly. If a player reaches 0 points the game is over. If a player has more than 0 points they decide if they want to keep playing. If a player decides not to play again the game is over.


### Project Structure

    .
    ├── .gitignore
    ├── hilo
    │   ├── __main__.py         # The initial launch file
    │   └── game 
    │       ├── director.py     # Directs the game action
    │       └── hilo.py         # performs the game action
    └── README.md


## Required Technologies

- Python 3.10.0


## Rules

- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.


## Requirements

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least two classes.
- The program must remain true to game play described in the overview.


## Things to do for fun:

- Enhanced input validation.
- Enhanced game play and game over messages.
- Enhanced game display, e.g. card suits

# Summary
This Hangman game is a simple command-line implementation where players guess letters to try to deduce a hidden word. The game can be played against the computer or by multiple human players.

## Features
- Players (human and AI) guess letters to form a word.
- Human players input their guesses.
- AI players randomly guess letters that haven't been tried yet.
- The game tracks each player's remaining lives and score.

## Classes
- `HMPlayer`: Base class for a player.
- `HMHumanPlayer`: Derived class for human players.
- `HMAIPlayer`: Derived class for AI players.
- `HMGame`: Class to manage the game setup, play, and determine the winner.

## How to Run
To run the game, simply execute the Python script. You may customize player names and modify the list of possible words directly in the script.

## Example Gameplay
1. The game is initialized with a list of players.
2. Each player takes turns guessing letters.
3. Incorrect guesses result in a loss of lives.
4. The game continues until the word is guessed or lives run out.
5. Scores are calculated based on correct guesses.

Ensure you have Python installed on your system to run this game. 

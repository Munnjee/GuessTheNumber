# Number Guessing Game

This is a simple number guessing game implemented in Python. The game generates a random number between 1 and 100, and the player's goal is to guess that number within a certain number of attempts based on the chosen difficulty level.

## Requirements

- Python 3.x

## Usage

1. Run the `main.py` file using Python.
   ```
   python main.py
   ```

2. The game will display the logo and a welcome message.

3. Choose a difficulty level by typing 'easy' or 'hard'.

   - Easy: You have 10 attempts to guess the number.
   - Hard: You have 5 attempts to guess the number.

4. The game will prompt you to make a guess. Enter a number between 1 and 100.

   - If your guess is higher than the random number, the game will display "Too high!".
   - If your guess is lower than the random number, the game will display "Too low!".

5. Repeat step 4 until you guess the correct number or run out of attempts.

6. If you guess the correct number within the given attempts, you win and the game will display a victory message.

7. If you run out of attempts without guessing the correct number, you lose and the game will display a defeat message.

8. After each game, you will be prompted to play again. Type 'y' to play another round or 'n' to exit the game.

## Files

The code is organized into two files:

- `main.py`: Contains the main logic of the number guessing game.
- `art.py`: Contains ASCII art used in the game.

## ASCII Art

The game uses ASCII art for the logo, victory message, and defeat message. The ASCII art is defined in the `art.py` file and imported into the `main.py` file for display.
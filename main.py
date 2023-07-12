import random
import art
import os


def set_difficulty():
    attempts = 0

    while attempts == 0:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy':
            return 10
        elif level == 'hard':
            return 5
        else:
            print("You have entered an invalid value, try again.\n")


def play():
    print(art.logo)

    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

    attempts = set_difficulty()

    random_number = random.randint(1, 100)
    guess = 0

    while attempts > 0 and guess != random_number:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("\nToo high!")
        elif guess < random_number:
            print("\nToo low!")
        attempts -= 1
        if attempts > 0:
            print("Guess again.\n")

    if guess == random_number:
        print(art.win)
        print(f"\nYou got it! the answer was {random_number}\n")
    else:
        print(art.lose)
        print("\nYou've run out of guesses, you lose!\n")


while input("Do you want to play a number guessing game? Type 'y' or 'n': "
            ) == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play()

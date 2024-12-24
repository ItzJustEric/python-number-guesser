import random
from game2 import computer_guess

def userGuess():
    range = input("What would you like the range to be: ")

    random_num = random.randint(0, int(range))

    attempts = 0
    while attempts < 3 :
        guess = input("Guess the number: ")
        if int(guess) == random_num:
            print("You guessed it correctly!")
            break

        elif int(guess) > random_num:
            print("Guess was too high!")

        else:
            print("Guess was too low!")

        attempts += 1

        if attempts == 3:
            print(f"You ran out of guesses. The number was {random_num}")

keep_playing = True
while keep_playing:

    play_game = input("would you like to continue playing?: (yes)/(no)")
    if play_game == "no":
        print("okay thanks for playing!")
        break

    choose_game = input("Would you like to guess or have the computer guess? (computer/player): ")

    if choose_game == "computer":
        computer_guess()
    elif choose_game == "player":
        userGuess()
    else:
        print("Invalid choice, please select 'computer' or 'player'.")

import random


def computer_guess():
    lower_limit = 0
    upper_limit = 10
    attempts = 0
    while attempts < 3:



        print(f"think of a number {lower_limit} to {upper_limit} and I will try to guess it ")

        ai_number = random.randint(lower_limit,upper_limit)

        guess = input(f"Is the number {ai_number}  (Respond with: too high, too low, or correct): ")



        if guess == "correct":
            print(f"I guessed it in {attempts + 1} tries")
            break

        elif guess =="too high":
            upper_limit = ai_number - 1

        else:
            lower_limit = ai_number + 1

        attempts += 1

        if attempts == 3:
            print(f"I ran out of guesses")




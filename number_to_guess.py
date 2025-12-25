import random


def number_to_guess():
    import random

    number_to_guess = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("To high!")
            else:
                print("Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Please enter a valid integer.")


# Run all sections sequentially
print("\n=== Number Guessing Game ===")
number_to_guess()

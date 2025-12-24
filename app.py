import random
from datetime import datetime


def greet_user():
    """Prompt the user for their name and greet them."""
    name = input("Please enter your name: ")
    if not name.strip():
        name = "there"  # default greeting if no name provided
    print(f"Hello, {name}! Nice to meet you.")


def calculate_age():
    """Ask for birth year and calculate the user's age."""
    current_year = datetime.now().year
    while True:
        year_str = input("Enter your birth year: ")
        try:
            birth_year = int(year_str.strip())
        except ValueError:
            print("That's not a valid year. Please enter a number.")
            continue
        # Defensive check for realistic year:
        if birth_year <= 0:
            print("Year must be a positive number. Try again.")
            continue
        if birth_year > current_year:
            print("You entered a future year. Please enter your actual birth year.")
            continue
        age = current_year - birth_year
        print(f"You are {age} years old in {current_year}.")
        break


def convert_weight():
    """Ask for weight and unit, then convert to the other unit (kg <-> lbs)."""
    while True:
        weight_str = input("Enter your weight: ")
        try:
            weight = float(weight_str.strip())
        except ValueError:
            print("That's not a valid number. Please enter your weight in digits.")
            continue
        if weight <= 0:
            print("Weight must be a positive number. Try again.")
            continue
        unit = input("Is that weight in (K)g or (L)bs? ").strip().lower()
        if unit == "":
            print("Please specify the unit as 'K' for kilograms or 'L' for pounds.")
            continue
        unit_char = unit[0]
        if unit_char == "k":
            # weight given in kilograms, convert to pounds
            converted = weight * 2.20462
            print(f"Your weight in pounds is {converted:.2f} lbs.")
        elif unit_char == "l":
            # weight given in pounds, convert to kilograms
            converted = weight / 2.20462
            print(f"Your weight in kilograms is {converted:.2f} kg.")
        else:
            print("Invalid unit. Please enter 'K' for kg or 'L' for lbs.")
            continue
        # If we got here, conversion was successful
        break


def add_numbers():
    """Ask for two numbers and output their sum."""
    num1 = None
    # Get first number
    while num1 is None:
        num1_str = input("Enter the first number: ")
        try:
            num1 = float(num1_str.strip())
        except ValueError:
            print("That's not a valid number. Try again.")
            num1 = None
    num2 = None
    # Get second number
    while num2 is None:
        num2_str = input("Enter the second number: ")
        try:
            num2 = float(num2_str.strip())
        except ValueError:
            print("That's not a valid number. Try again.")
            num2 = None
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


def dice_game():
    """Run a dice-rolling game where two dice are rolled until the user stops."""
    roll_counter = 0
    total_score = 0
    while True:
        choice = input("Do you want to roll the dice? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2
            roll_counter += 1
            total_score += total
            print(
                f"Roll {roll_counter}: You rolled a {die1} and a {die2}. Total = {total}."
            )
            print(f"   (Current score: {total_score})")
        elif choice in ["no", "n"]:
            break
        else:
            print("Please answer 'yes' or 'no'.")
    # After exiting the loop, show summary
    print(f"You rolled the dice {roll_counter} times. Total score = {total_score}.")
    print("Dice game over.")
    # Keep the program open at the end
    try:
        input("Press Enter to continue...")
    except Exception:
        pass


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
if __name__ == "__main__":
    print("=== Welcome and Greeting ===")
    greet_user()
    print("\n=== Age Calculation ===")
    calculate_age()
    print("\n=== Weight Converter ===")
    convert_weight()
    print("\n=== Addition Calculator ===")
    add_numbers()
    print("\n=== Dice Rolling Game ===")
    dice_game()
    print("\n=== Number Guessing Game ===")
    number_to_guess()

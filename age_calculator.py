from datetime import datetime


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


# Run all sections sequentially
print("\n=== Age Calculation ===")
calculate_age()

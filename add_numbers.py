import random


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

    # Run all sections sequentially
    print("\n=== Addition Calculator ===")
    add_numbers()

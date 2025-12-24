import random
from datetime import datetime


def greet_user():
    """Prompt the user for their name and greet them."""
    name = input("Please enter your name: ")
    if not name.strip():
        name = "there"  # default greeting if no name provided
    print(f"Hello, {name}! Nice to meet you.")


# Run all sections sequentially
if __name__ == "__main__":
    print("=== Welcome and Greeting ===")
    greet_user()

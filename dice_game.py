import random


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


# Run all sections sequentially
print("\n=== Dice Rolling Game ===")
dice_game()

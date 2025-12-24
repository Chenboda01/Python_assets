import random
import math
import datetime


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


# Run all sections sequentially
if __name__ == "__main__":
    convert_weight()
    print("\n=== Weight Converter ===")

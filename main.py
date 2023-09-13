import random


def roll_dice(sides, num_rolls):
    return [random.randint(1, sides) for _ in range(num_rolls)]


while True:
    print("Choose a dice to roll (d4, d6, d8, d10, d12, d20) and "
          "enter the number of dice to roll, or type 'quit' to exit:")
    input_string = input()

    if input_string.lower() == 'quit':
        break

    sets = input_string.split(',')

    for dice_set in sets:
        parts = dice_set.split()

        if len(parts) == 2 and parts[1].lower() in ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']:
            num_rolls = int(parts[0])  # Extract the number of sides from the choice (e.g., 'd6' -> 6)
            sides = int(parts[1][1:])

            if num_rolls <= 0:
                print("Please enter a valid number of dice to roll.")
            else:
                results = roll_dice(sides, num_rolls)
                total = sum(results)
                print(f"You rolled {num_rolls} {parts[1]}: {results}")
                print(f"Total: {total}")
        else:
            print("Invalid choice. Please enter a dice from the options "
                  "and the number of dice to roll, or 'quit'.")

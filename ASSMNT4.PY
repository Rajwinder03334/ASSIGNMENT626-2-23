import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():

    num_sides = int(input("Enter the number of sides on the dice: "))


    max_number = int(input(f"Enter the maximum number on the {num_sides}-sided dice: "))

    while True:

        result = roll_dice(num_sides)


        print(f"Dice roll result: {result}")


        if result == max_number:
            print(f"You rolled the maximum number on a {num_sides}-sided dice: {max_number}!")
            break

if __name__ == "__main__":
    main()
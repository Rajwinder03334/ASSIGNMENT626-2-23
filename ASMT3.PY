import random

def roll_dice():
    return random.randint(2, 7)

def main():
    while True:

        result = roll_dice()


        print(f"Dice roll result: {result}")


        if result == 7:
            print("You rolled a 7!")
            break

if __name__ == "__main__":
    main()
import random

def roll_dice(num_dice):
    total = 0
    for _ in range(num_dice):

        roll_result = random.randint(1, 6)
        total += roll_result
        print(f"Rolling die: {roll_result}")

    return total

def main():

    num_dice = int(input("How many dice to roll? "))


    total_sum = roll_dice(num_dice)


    print(f"Total sum of {num_dice} dice: {total_sum}")

if __name__ == "__main__":
    main()
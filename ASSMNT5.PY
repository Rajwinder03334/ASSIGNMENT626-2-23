def gallons_to_liters(gallons):
    liters_per_gallon = 58.871
    return gallons * liters_per_gallon

def main():
    while True:

        gallons = float(input("Enter the quantity of gasoline in gallons (negative to exit): "))


        if gallons < 0:
            print("Exiting the program.")
            break


        liters = gallons_to_liters(gallons)


        print(f"{gallons} gallons is equal to {liters:.2f} liters.")

if __name__ == "__main__":
    main()
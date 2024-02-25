def remove_odd_numbers(original_list):

    even_numbers = [num for num in original_list if num % 2 == 0]
    return even_numbers

def main():

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    cut_down_list = remove_odd_numbers(original_list)


    print("Original List:", original_list)
    print("Cut-down List:", cut_down_list)

if __name__ == "__main__":
    main()
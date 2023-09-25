#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integers printed
    
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()  # Print a newline after printing the integers
    except (IndexError, TypeError) as e:
        print(e)  # Print the error message when an exception occurs
    
    return count

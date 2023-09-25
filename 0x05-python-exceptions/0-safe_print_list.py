#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()  # Print a newline after printing the elements
        return count
    except IndexError:
        # Handle the exception when x is greater than the length of my_list
        print()
        return count

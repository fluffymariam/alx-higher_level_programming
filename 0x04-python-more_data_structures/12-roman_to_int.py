#!/usr/bin/python3

def roman_to_int(roman_string):
    # Define a dictionary to map Roman numerals to their integer values
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result
    result = 0
    
    # Initialize a variable to keep track of the previous numeral's value
    prev_value = 0
    
    # Iterate over the Roman numeral string in reverse order
    for numeral in reversed(roman_string):
        # Get the integer value of the current numeral
        current_value = roman_dict[numeral]
        
        # If the current numeral's value is less than the previous numeral's value,
        # subtract it from the result; otherwise, add it to the result
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        # Update the previous numeral's value
        prev_value = current_value
    
    return result

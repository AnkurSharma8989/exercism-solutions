"""
    Determine whether a given number is an Armstrong number.
"""

def is_armstrong_number(number):
    """
    Check whether the given number is an Armstrong number.

    :param number: The integer to check.
    :return: True if the number is an Armstrong number, otherwise False.
    """
    number_str = str(number)
    total = 0
    number_length = len(number_str)
    
    for each_one in number_str:
        total += int(each_one) ** number_length
        
    return total == number
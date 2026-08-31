"""
    Determine whether a given number is an Armstrong number.
"""

def is_armstrong_number(number):
    """
    Check whether the given number is an Armstrong number.

    :param number: The integer to check.
    :return: True if the number is an Armstrong number, otherwise False.
    """
    numberstr = str(number)
    total = 0
    numberlength = len(numberstr)
    
    for eachone in numberstr:
        total += pow(int(eachone),numberlength)
        
    return total == number
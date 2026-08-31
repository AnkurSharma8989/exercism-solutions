"""
    Calculate the number of steps required for a positive integer to reach 1 using the Collatz Conjecture.
"""

def steps(number):
    """
        This function accepts a positive integer and returns the number of steps it takes to reach 1, or            raises an error if the number is not positive.
        param number: positive integer
        return: number of steps required to reach 1
    """
    if number <= 0 :
        raise ValueError("Only positive integers are allowed")

    steps_count = 0

    while number > 1 :
        if number % 2 == 0:
            number = number // 2
        else:
            number = number*3 + 1
        steps_count += 1

    return steps_count
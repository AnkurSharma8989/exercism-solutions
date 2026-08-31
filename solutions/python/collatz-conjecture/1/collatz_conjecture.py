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

    stepscount = 0
    currentnumber = number

    while(currentnumber > 1):
        if currentnumber % 2 == 0:
            currentnumber = currentnumber // 2
        else:
            currentnumber = currentnumber*3 + 1
        stepscount += 1

    return stepscount

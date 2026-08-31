'''
    This is a program to calculate chess baord and square and grain
'''

def square(number):
    '''
        This function calculates the grains on a given square.,
        Parameters:
            number (int): Chessboard square.
    '''
    if not isinstance(number, int):
        raise TypeError("Sqaure must be an integer value")
    if number<1 or number >64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    '''
        This function give the total number of grains on chess board
    '''
    return pow(2,64)-1
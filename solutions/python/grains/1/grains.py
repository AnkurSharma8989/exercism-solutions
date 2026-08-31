def square(number):
    '''
        This function sqaures the given number,
        parameter number: int
    '''
    if not isinstance(number, int):
        raise TypeError("Sqaure must be an integer value")
    if number<1 or number >64:
        raise ValueError("square must be between 1 and 64")
    if number==1:
        return 1
    else:
        return pow(2,number-1)


def total():
    '''
        This function give the total number of grains on chess board
    '''
    sqo = 1
    total = 0
    while sqo <= 64 and sqo >= 1:
        current = pow(2,sqo-1)
        total += current
        sqo+=1
    return total
    

"""
    Convert a number into its corresponding raindrop sounds.
"""
def convert(number):
    """
    Convert a number into a string based on its divisibility by 3, 5, and 7.

    :param number: The number to convert.
    :return: Raindrop sounds or the number as a string if it is not divisible by 3, 5, or 7.
    """    
    result = ""
    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if not 0 in (number % 3, number % 5, number % 7):
        result = str(number)
    return result
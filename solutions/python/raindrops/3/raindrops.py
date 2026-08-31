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
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    
    if result == "":
        return str(number)
    return result
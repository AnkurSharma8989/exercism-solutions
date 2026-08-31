"""
    Classify a positive integer as perfect, abundant, or deficient.
"""
def classify(number):
    """
    Classify a positive integer as perfect, abundant, or deficient.

    :param number: The positive integer to classify.
    :return: "perfect", "abundant", or "deficient" based on the aliquot sum.
    :raises ValueError: If number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    sum_of_factors = 0

    for factor in range(1,number//2 + 1):
        if number % factor == 0:
            sum_of_factors += factor

    if sum_of_factors == number:
        return "perfect"
    if sum_of_factors > number:
        return "abundant"
    return "deficient"
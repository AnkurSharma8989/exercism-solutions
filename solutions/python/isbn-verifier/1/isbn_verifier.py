"""
    Determine whether an ISBN-10 is valid.
"""
def is_valid(isbn):
    """
    Check whether the given string is a valid ISBN-10.

    :param isbn: The ISBN-10 string to validate.
    :return: True if the ISBN-10 is valid, otherwise False.
    """
    isbn_removed = isbn.replace("-","")
    for eachnum in isbn_removed:
        if eachnum not in "0123456789X":
            return False
    if len(isbn_removed) == 10 and "X" not in isbn_removed[:-1]:
        weight = 10
        check_sum = 0
        for eachnum in isbn_removed[:-1]:
            check_sum += weight * int(eachnum)
            weight -= 1
        if isbn_removed[-1] == "X":
            check_sum += 10
        else:
            check_sum += int(isbn_removed[-1])
    else:
        return False
    return check_sum % 11 == 0
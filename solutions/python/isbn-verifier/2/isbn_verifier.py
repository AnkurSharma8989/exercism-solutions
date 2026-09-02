"""
    Determine whether an ISBN-10 is valid.
"""
def is_valid(isbn):
    """
    Check whether the given string is a valid ISBN-10.

    :param isbn: The ISBN-10 string to validate.
    :return: True if the ISBN-10 is valid, otherwise False.
    """
    # Solution 1 - my
    # cleaned_isbn = isbn.replace("-","")
    # for eachnum in cleaned_isbn:
    #     if eachnum not in "0123456789X":
    #         return False
    # if len(cleaned_isbn) == 10 and "X" not in cleaned_isbn[:-1]:
    #     weight = 10
    #     check_sum = 0
    #     for eachnum in cleaned_isbn[:-1]:
    #         check_sum += weight * int(eachnum)
    #         weight -= 1
    #     if cleaned_isbn[-1] == "X":
    #         check_sum += 10
    #     else:
    #         check_sum += int(cleaned_isbn[-1])
    # else:
    #     return False
    # return check_sum % 11 == 0

    cleaned_isbn = isbn.replace("-", "")
    check_sum = 0
    
    if len(cleaned_isbn) != 10:
        return False
    
    for weight, digit in zip(range(10,0,-1), cleaned_isbn):
        if digit not in "0123456789X" or (weight != 1 and digit == "X"):
            return False
        if digit == "X":
            check_sum += 10
        else:
            check_sum += weight * int(digit)

    return check_sum % 11 == 0
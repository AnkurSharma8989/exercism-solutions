"""
    Determine whether a word or phrase is an isogram.
"""
import string
def is_isogram(phrase):
    """
    Check whether a word or phrase contains no repeated letters.

    :param phrase: The word or phrase to check.
    :return: True if no letter is repeated, otherwise False.
    """
    # Solution - 1 my
    # for word in phrase.lower():
    #     if word in string.ascii_lowercase:
    #         count_char = (phrase.lower()).count(word)
    #         if count_char > 1:
    #             return False
    # return True

    letters = [char for char in phrase.lower() if char in string.ascii_lowercase]
    return len(letters) == len(set(letters))
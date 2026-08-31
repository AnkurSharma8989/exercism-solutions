"""
    Determine whether a word or phrase is an isogram.
"""
def is_isogram(phrase):
    """
    Check whether a word or phrase contains no repeated letters.

    :param phrase: The word or phrase to check.
    :return: True if no letter is repeated, otherwise False.
    """
    for word in phrase.lower():
        if word in "abcdefghijklmnopqrstuvwxyz":
            count_char = (phrase.lower()).count(word)
            if count_char > 1:
                return False
            continue

    return True
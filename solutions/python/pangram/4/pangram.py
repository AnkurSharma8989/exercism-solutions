import string
"""
    Determine whether a sentence is a pangram.
"""
def is_pangram(sentence):
    """
    Check whether a sentence contains every letter of the English alphabet.

    :param sentence: The sentence to check.
    :return: True if the sentence contains all 26 letters, otherwise False.
    """
    if not sentence:
        return False
    
    sentence_check = sentence.lower()

    for letter in string.ascii_lowercase:
        if letter not in sentence_check:
            return False

    return True
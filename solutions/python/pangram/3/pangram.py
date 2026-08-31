"""
    Determine whether a sentence is a pangram.
"""
def is_pangram(sentence):
    """
    Check whether a sentence contains every letter of the English alphabet.

    :param sentence: The sentence to check.
    :return: True if the sentence contains all 26 letters, otherwise False.
    """
    if sentence == "":
        return False
    pangram_check = "abcdefghijklmnopqrstuvwxyz"
    sentence_check = sentence.lower()

    for word_check in pangram_check:
        if word_check in sentence_check:
            continue
        return False

    return True
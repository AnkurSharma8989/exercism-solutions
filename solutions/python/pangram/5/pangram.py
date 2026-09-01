"""
    Determine whether a sentence is a pangram.
"""
import string

def is_pangram(sentence):
    """
    Check whether a sentence contains every letter of the English alphabet.

    :param sentence: The sentence to check.
    :return: True if the sentence contains all 26 letters, otherwise False.
    """
    # Solution 1 - my
    # if sentence == "":
    #     return False
    # pangram_check = "abcdefghijklmnopqrstuvwxyz"
    # sentence_check = sentence.lower()

    # for word_check in pangram_check:
    #     if word_check in sentence_check:
    #         continue
    #     return False

    # return True
    
    # Solution 2 - mentor fb
    # if not sentence:
    #     return False
    
    # sentence_check = sentence.lower()

    # for letter in string.ascii_lowercase:
    #     if letter not in sentence_check:
    #         return False

    # return True

    # Solution 3 - as per exercism recomendation
    return all(letter in sentence.lower() for letter in string.ascii_lowercase)
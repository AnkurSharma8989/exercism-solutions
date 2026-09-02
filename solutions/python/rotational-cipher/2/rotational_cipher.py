"""
    Encrypt text using a rotational cipher.
"""
import string
def rotate(text, key):
    """
    Shift each letter in the text by the given rotational key.

    :param text: The text to encrypt.
    :param key: The number of positions to rotate each letter.
    :return: The encrypted text with its original formatting preserved.
    """
    # Solution 1 -my    
    # plain_key_lower = "abcdefghijklmnopqrstuvwxyz"
    # cipher_key_lower = plain_key_lower[key:] + plain_key_lower[:key]
    # plain_key_upper = plain_key_lower.upper()
    # cipher_key_upper = plain_key_upper[key:] + plain_key_upper[:key]
    # cipher_text = ""

    # for eachletter in text:
    #     if eachletter not in plain_key_lower and eachletter not in plain_key_upper:
    #         cipher_text += eachletter
    #     elif eachletter in plain_key_upper:
    #         cipher_text += cipher_key_upper[plain_key_upper.find(eachletter)]
    #     else:
    #         cipher_text += cipher_key_lower[plain_key_lower.find(eachletter)]

    # return cipher_text

    # Solution 2 - also my but with updated concepts

    cipher_key_lower = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    cipher_key_upper = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    cipher_text = ""

    for eachletter in text:
        if not eachletter.isalpha():
            cipher_text += eachletter
        elif eachletter in string.ascii_uppercase:
            cipher_text += cipher_key_upper[string.ascii_uppercase.find(eachletter)]
        else:
            cipher_text += cipher_key_lower[string.ascii_lowercase.find(eachletter)]

    return cipher_text
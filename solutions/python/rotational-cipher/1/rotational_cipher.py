"""
    Encrypt text using a rotational cipher.
"""
def rotate(text, key):
    """
    Shift each letter in the text by the given rotational key.

    :param text: The text to encrypt.
    :param key: The number of positions to rotate each letter.
    :return: The encrypted text with its original formatting preserved.
    """
    plain_key_lower = "abcdefghijklmnopqrstuvwxyz"
    cipher_key_lower = plain_key_lower[key:] + plain_key_lower[:key]
    plain_key_upper = plain_key_lower.upper()
    cipher_key_upper = plain_key_upper[key:] + plain_key_upper[:key]
    cipher_text = ""

    for eachletter in text:
        if eachletter not in plain_key_lower and eachletter not in plain_key_upper:
            cipher_text += eachletter
        elif eachletter in plain_key_upper:
            cipher_text += cipher_key_upper[plain_key_upper.find(eachletter)]
        else:
            cipher_text += cipher_key_lower[plain_key_lower.find(eachletter)]

    return cipher_text
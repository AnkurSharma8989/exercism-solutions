"""
    Reverse a given string.
"""
def reverse(text):
    """
    Reverse the characters in a given string.

    :param text: The string to reverse.
    :return: The reversed string.
    """   
    # Solution 1 - my
    # reversetext = ""
    # for reverse_len in range(len(text)-1, -1, -1):
    #     reversetext += text[reverse_len]
    # return reversetext

    # Solution 2 - mentor
    # return text[::-1]

    # Solution 3 - mentor
    return ''.join(reversed(text))
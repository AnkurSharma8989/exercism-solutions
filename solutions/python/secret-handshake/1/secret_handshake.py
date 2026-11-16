"""
Convert a binary string into a sequence of secret handshake actions.
"""
def commands(binary_str):
    """
    Translate a 5-digit binary string into a list of secret handshake commands.

    :param binary_str: A string of 5 binary digits (e.g., "00011").
    :return: A list of strings representing the actions in the correct order.
    """    
    final_code = []
    for index, letter in enumerate(binary_str[::-1]):
        if letter == "1" and index == 0:
            final_code.append("wink")
        elif letter == "1" and index == 1:
            final_code.append("double blink")
        elif letter == "1" and index == 2:
            final_code.append("close your eyes")
        elif letter == "1" and index == 3:
            final_code.append("jump")
        elif letter == "1" and index == 4:
            final_code = final_code[::-1]
    
    return final_code
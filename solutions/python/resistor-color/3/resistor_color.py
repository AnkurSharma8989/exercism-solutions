"""
Convert resistor band colors into their corresponding numerical values and return the list of available resistor colors.
"""

def color_code(color):
    """
    Return the numerical value associated with a resistor color.

    :param color: The resistor band color to look up.
    :return: The numerical value of the color.
    """
    resistor_color = colors()
    if color in resistor_color:
        return resistor_color.index(color)
    else:
        raise ValueError("Enter valid color")


def colors():
    """
    Return the list of resistor band colors in numerical order.

    :return: The list of resistor colors from black to white.
    """
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return resistor_color
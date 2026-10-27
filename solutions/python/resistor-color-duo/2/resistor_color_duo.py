"""
Convert the first two resistor band colors into a two-digit resistance value.
"""


def value(colors):
    """
    Return the numerical value represented by the first two resistor colors.

    :param colors: A list of resistor band color names.
    :return: The first two-digit resistance value formed by the first two colors.
    """
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    resistance = ""
    for color in colors[0:2]:
        resistance += str(resistor_color.index(color))
    return int(resistance)
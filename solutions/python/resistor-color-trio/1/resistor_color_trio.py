"""
Calculate the resistance value in ohms from three resistor color bands, including metric prefixes.
"""

def label(colors):
    """
    Return the formatted resistance value and its metric prefix based on three color bands.

    :param colors: A list of three resistor band color names.
    :return: A string representing the total resistance with the appropriate metric prefix (e.g., "33 kiloohms").
    """
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    final_output = ((resistor_color.index(colors[0]) * 10) + resistor_color.index(colors[1])) * (10 ** resistor_color.index(colors[2]))
    
    if final_output >= 1000000000:
        return str(final_output//1000000000) + " gigaohms"
    if final_output >= 1000000:
        return str(final_output//1000000) + " megaohms"
    if final_output >= 1000:
        return str(final_output//1000) + " kiloohms"
    return str(final_output) + " ohms"
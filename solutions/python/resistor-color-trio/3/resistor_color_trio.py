"""
Calculate the resistance value in ohms from three resistor color bands, including metric prefixes.
"""
COLOR_VALUES = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
UNITS = (
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
    (1, "ohms")
)


def label(colors: list[str]) -> str:
    """
    Return the formatted resistance value and its metric prefix based on three color bands.

    :param colors: A list of three resistor band color names.
    :return: A string representing the total resistance with the appropriate metric prefix (e.g., "33 kiloohms").
    """
    #Solution 1 - 
    # resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    # final_output = ((resistor_color.index(colors[0]) * 10) + resistor_color.index(colors[1])) * (10 ** resistor_color.index(colors[2]))
    
    # if final_output >= 1000000000:
    #     return str(final_output//1000000000) + " gigaohms"
    # if final_output >= 1000000:
    #     return str(final_output//1000000) + " megaohms"
    # if final_output >= 1000:
    #     return str(final_output//1000) + " kiloohms"
    # return str(final_output) + " ohms"
    
    first_digit = COLOR_VALUES.index(colors[0])
    second_digit = COLOR_VALUES.index(colors[1])
    multiplier = COLOR_VALUES.index(colors[2])
    
    value = (first_digit * 10 + second_digit) * 10 ** multiplier
    
    for divisor, unit in UNITS:
        if value >= divisor:
            return f"{value//divisor} {unit}"

    return "0 ohms"
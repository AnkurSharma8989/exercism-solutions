"""
Calculate the resistance value and TOLERANCE from 1, 4, or 5 resistor color bands.
"""
COLOR_VALUE = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
    
TOLERANCE = {
        "grey": "0.05%", "violet" : "0.1%", "blue" : "0.25%", "green" : "0.5%", "brown" : "1%", "red" : "2%", "gold" : "5%", "silver" : "10%"
    }

PREFIX = ("ohms", "kiloohms", "megaohms", "gigaohms")

def resistor_label(colors):
    """
    Return the formatted resistance value, metric prefix, and TOLERANCE percentage.

    :param colors: A list of 1, 4, or 5 resistor band color names.
    :return: A string representing the total resistance and TOLERANCE (e.g., "33 ohms ±0.5%").
    """
    
    if len(colors) == 1:
        return "0 ohms"

    #Solution 1
    # if len(colors) == 1:
    #     return "0 ohms"
    
    # resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    # tolerance = {
    #     "grey": "0.05%", "violet" : "0.1%", "blue" : "0.25%", "green" : "0.5%", "brown" : "1%", "red" : "2%", "gold" : "5%", "silver" : "10%"
    # }
    
    # final_resistance = 0
    # value = ""
    # prefix = ""
    
    # if len(colors) == 4:
    #     final_resistance = ((resistor_color.index(colors[0]) * 10) + resistor_color.index(colors[1])) * (10 ** resistor_color.index(colors[2]))
    # elif len(colors) == 5:
    #     final_resistance = ((resistor_color.index(colors[0]) * 100) + (resistor_color.index(colors[1]) * 10) + resistor_color.index(colors[2])) * (10 ** resistor_color.index(colors[3]))

    # if final_resistance >= 1000000000:
    #     value = final_resistance/1000000000
    #     prefix = " gigaohms ±" + tolerance[colors[-1]]
        
    # elif final_resistance >= 1000000:
    #     value = final_resistance/1000000
    #     prefix = " megaohms ±" + tolerance[colors[-1]]
        
    # elif final_resistance >= 1000:
    #     value = final_resistance/1000
    #     prefix = " kiloohms ±" + tolerance[colors[-1]]

    # else:
    #     value = final_resistance
    #     prefix = " ohms ±" + tolerance[colors[-1]]
        
    # if value % 1 == 0:
    #     value = str(int(value))
    # else:
    #     value = str(value)
    
    # return value + prefix

    resistance_value = 0
    for color in colors[:-2]:
        resistance_value = resistance_value * 10 + COLOR_VALUE.index(color)

    multiplier = COLOR_VALUE.index(colors[-2])

    resistance = resistance_value * 10 ** multiplier

    unitindex = 0
    
    while resistance >= 1000:
        resistance /= 1000
        unitindex += 1

    return (f"{resistance:g} {PREFIX[unitindex]} ±{TOLERANCE[colors[-1]]}" )
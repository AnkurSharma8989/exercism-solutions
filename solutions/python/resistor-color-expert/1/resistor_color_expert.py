"""
Calculate the resistance value and tolerance from 1, 4, or 5 resistor color bands.
"""
def resistor_label(colors):
    """
    Return the formatted resistance value, metric prefix, and tolerance percentage.

    :param colors: A list of 1, 4, or 5 resistor band color names.
    :return: A string representing the total resistance and tolerance (e.g., "33 ohms ±0.5%").
    """
    
    if len(colors) == 1:
        return "0 ohms"
    
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    tolerance = {
        "grey": "0.05%", "violet" : "0.1%", "blue" : "0.25%", "green" : "0.5%", "brown" : "1%", "red" : "2%", "gold" : "5%", "silver" : "10%"
    }
    
    final_resistance = 0
    value = ""
    prefix = ""
    
    if len(colors) == 4:
        final_resistance = ((resistor_color.index(colors[0]) * 10) + resistor_color.index(colors[1])) * (10 ** resistor_color.index(colors[2]))
    elif len(colors) == 5:
        final_resistance = ((resistor_color.index(colors[0]) * 100) + (resistor_color.index(colors[1]) * 10) + resistor_color.index(colors[2])) * (10 ** resistor_color.index(colors[3]))

    if final_resistance >= 1000000000:
        if (final_resistance/1000000000) % 1 == 0:
            value = str(int(final_resistance/1000000000))
        else:
            value = str(final_resistance/1000000000)
        prefix = " gigaohms ±" + tolerance[colors[-1]]
        
    elif final_resistance >= 1000000:
        if (final_resistance/1000000) % 1 == 0:
            value = str(int(final_resistance/1000000))
        else:
            value = str(final_resistance/1000000)
        prefix = " megaohms ±" + tolerance[colors[-1]]
        
    elif final_resistance >= 1000:
        if (final_resistance/1000) % 1 == 0:
            value = str(int(final_resistance/1000))
        else:
            value = str(final_resistance/1000)
        prefix = " kiloohms ±" + tolerance[colors[-1]]

    else:
        value = str(final_resistance)
        prefix = " ohms ±" + tolerance[colors[-1]]
        
    return value + prefix
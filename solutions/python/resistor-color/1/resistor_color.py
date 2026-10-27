def color_code(color):
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    if color in resistor_color:
        return resistor_color.index(color)
    else:
        return ("Enter valid color")

def colors():
    resistor_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return resistor_color
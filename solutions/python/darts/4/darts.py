"""
    Calculate the score earned by a dart based on its distance from the center of the target.
"""
def score(x_axis, y_axis):
    """
    Calculate the points scored by a dart at the given coordinates.

    :param x: The x-coordinate of the dart.
    :param y: The y-coordinate of the dart.
    :return: The score based on the dart's distance from the center.
    """
    distance_from_center = x_axis ** 2 + y_axis ** 2
    if distance_from_center <= 1:
        return 10
    if distance_from_center <= 25:
        return 5
    if distance_from_center <= 100:
        return 1
    return 0
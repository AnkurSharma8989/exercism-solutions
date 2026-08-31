"""
    Calculate the score earned by a dart based on its distance from the center of the target.
"""
def score(x, y):
    """
    Calculate the points scored by a dart at the given coordinates.

    :param x: The x-coordinate of the dart.
    :param y: The y-coordinate of the dart.
    :return: The score based on the dart's distance from the center.
    """
    distance_from_center = x ** 2 + y ** 2
    if 25 < distance_from_center <= 100:
        return 1
    if 1 < distance_from_center <= 25:
        return 5
    if distance_from_center <= 1:
        return 10
    return 0
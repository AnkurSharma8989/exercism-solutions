def score(x, y):
    distance_from_center = x ** 2 + y ** 2
    if distance_from_center <= 100 and distance_from_center > 25:
        return 1
    if distance_from_center <= 25 and distance_from_center > 1:
        return 5
    if distance_from_center <= 1:
        return 10
    return 0
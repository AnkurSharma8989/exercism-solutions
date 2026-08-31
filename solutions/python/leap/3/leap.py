"""
    Check if a year is leap year or not
"""
def leap_year(year):
    """
    Check if a year is leap year or not
    param year: takes year in int
    """
    if year%100==0:
        if year%400==0:
            return True
        return False
    if year%4==0:
        return True
    return False
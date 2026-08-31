"""
    Check if a year is leap year or not
"""
def leap_year(year):
    """
    Check if a year is leap year or not
    param year: takes year in int
    """
    return year%4 ==0 and (year%100!=0 or year%400==0)
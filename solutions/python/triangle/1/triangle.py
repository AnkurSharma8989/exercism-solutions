"""
    This code block tell you if triangle is equilateral, isosceles or scalene
"""

def equilateral(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a!=0 or b!=0 or c!=0:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if a==b and b==c and c==a:
                return True
    return False


def isosceles(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a!=0 or b!=0 or c!=0:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if (a==b or b==c) or a==c:
                return True
    return False


def scalene(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """    
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a!=0 or b!=0 or c!=0:
        if (a + b >= c) and (b + c >= a) and (a + c >= b):
            if a!=b and b!=c and a!=c :
                return True
    return False
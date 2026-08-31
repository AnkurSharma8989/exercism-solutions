"""
    This code block tell you if triangle is equilateral, isosceles or scalene
"""

def triangle_check(sides):
    """
    This code block test if the shape can be a traingle or not
    param sides: call list that have three value, use indexing to call each return true or false
    """
    if min(sides)>0:
        return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])
    return False

def equilateral(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    if triangle_check(sides):
        if sides[0]==sides[1] and sides[1]==sides[2]:
            return True
    return False


def isosceles(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    if triangle_check(sides):
        if (sides[0]==sides[1]) or (sides[1]==sides[2]) or (sides[0]==sides[2]):
            return True
    return False


def scalene(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """    
    if triangle_check(sides):
        if sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0]!=sides[2] :
            return True
    return False
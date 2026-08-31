"""
    This code block tell you if triangle is equilateral, isosceles or scalene
"""

def triangle_check(sides):
    """
    This code block test if the shape can be a traingle or not
    param sides: call list that have three value, use indexing to call each return true or false
    """
    side1, side2, side3 = sorted(sides)
    return side1 + side2 > side3

def equilateral(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    return triangle_check(sides) and len(set(sides)) == 1


def isosceles(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    return triangle_check(sides) and len(set(sides)) <= 2


def scalene(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """    
    return triangle_check(sides) and len(set(sides)) == 3
"""
    This code block tell you if triangle is equilateral, isosceles or scalene
"""

def equilateral(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    if side1!=0 or side2!=0 or side3!=0:
        if (side1 + side2 >= side3) and (side2 + side3 >= side1) and (side1 + side3 >= side2):
            if side1==side2 and side2==side3 and side3==side1:
                return True
    return False


def isosceles(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    if side1!=0 or side2!=0 or side3!=0:
        if (side1 + side2 >= side3) and (side2 + side3 >= side1) and (side1 + side3 >= side2):
            if (side1==side2 or side2==side3) or side1==side3:
                return True
    return False


def scalene(sides):
    """
    This code block tell you if triangle is equilateral, isosceles or scalene
    param sides: call list that have three value, use indexing to call each return true or false
    """    
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    if side1!=0 or side2!=0 or side3!=0:
        if (side1 + side2 >= side3) and (side2 + side3 >= side1) and (side1 + side3 >= side2):
            if side1!=side2 and side2!=side3 and side1!=side3 :
                return True
    return False
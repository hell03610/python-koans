#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
  
    check_parameters(a,b,c)  
    if(a == b and b == c): return 'equilateral'
    if (a == b or b == c or a == c): return 'isosceles'
    return 'scalene'

def check_parameters(a , b, c):
    if(a <= 0 or b <= 0 or c <= 0): raise TriangleError
    # check_triangle(a,b,c)

def check_triangle(a , b, c):
    sides = [a,b,c]
    maximum = max(sides)
    sides.remove(maximum)
    h = 0
    for side in sides:
        h += side*side
    h = h**0.5

    print h

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass

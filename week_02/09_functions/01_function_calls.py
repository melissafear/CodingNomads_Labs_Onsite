'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
import math


def rect_area(width, height):
    result = width * height
    return result

def circle_area(radius):
    result = math.pi*radius**2
    return result

def circle_perimeter(radius):
    result = 2 * math.pi*radius
    return result

def tube_surface_area(height, radius):
    result = rect_area(circle_perimeter(radius), height)
    return result

def cylinder_surface_area(height, radius):
    result = tube_surface_area(height, radius) + 2*(circle_area(radius))
    return result

print(cylinder_surface_area(10,5))

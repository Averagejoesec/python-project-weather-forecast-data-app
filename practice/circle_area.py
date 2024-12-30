import math

radius = float(input("Enter the radius of the circle: "))

def calculate_area(radius):
    area = math.pi * radius**2
    message = print(f"The are of a circle with a radius {radius} is {round(area, 2)}.")
    return message


calculate_area(radius)
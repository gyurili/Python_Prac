import math

def get_area(radius):
    area = math.pi * math.pow(radius, 2)
    return area


radius = 1.5

area = get_area(radius)
print(area)
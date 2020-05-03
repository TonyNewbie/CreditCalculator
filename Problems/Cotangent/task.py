import math


angle_degrees = int(input())
angle_radians = math.radians(angle_degrees)
print(round(1 / math.tan(angle_radians), 10))

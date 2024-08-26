import math

# all values are in milimeters

diameter = 9

# line_width = 0.3

line_length = 2 * 100 * 10

wraps = line_length / (diameter * math.pi)

print(wraps)

# Advent of Code: Day 6
# Manhattan Area

# Part 1: Finding the largest finite area using the Manhattan distance
from math import fabs

# The Manhattan Distance, also known as the L1 metric.
# Calculates the distance between two points (given as tuples) and returns a float.
def Dist_L1(a, b):
    return ( fabs(b[0]-a[0])+fabs(b[1]-a[1]) )
import numpy
import math

# Algoritma Brute Force untuk control point (n) = 3
def bezier_bf(points, iteration):
    precision = 1.0/2**iteration
    points_fix = [points[0]]  
    t = 0
    while t < 1:
        t += precision
        x = (1 - t)**2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t**2 * points[2][0]
        y = (1 - t)**2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t**2 * points[2][1]
        points_fix.append((x, y))  
    return points_fix
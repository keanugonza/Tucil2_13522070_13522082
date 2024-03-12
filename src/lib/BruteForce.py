import numpy
import math

# Algoritma Brute Force
def bezier_bf(points, precision=0.02):
    points_fix = [points[0]]  
    t = 0
    while t <= 1:
        x = (1 - t)**2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t**2 * points[2][0]
        y = (1 - t)**2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t**2 * points[2][1]
        t += precision
        points_fix.append((x, y))  
    points_fix.append(points[2]) 
    return points_fix
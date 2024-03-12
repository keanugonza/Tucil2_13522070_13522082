import numpy
import math

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Algoritma Divide and Conquer
def bezier_dnc(n, points, iterations):
    # Base case
    if iterations == 0:
        return [points[0], points[n - 1]]
    
    # Divide
    q0 = midpoint(points[0], points[1])
    q1 = midpoint(points[1], points[2])
    r0 = midpoint(q0, q1)
    
    # Conquer
    left_curve = bezier_dnc(n, [points[0], q0, r0], iterations - 1)
    right_curve = bezier_dnc(n, [r0, q1, points[2]], iterations - 1)
    
    return left_curve[:-1] + [r0] + right_curve[1:]
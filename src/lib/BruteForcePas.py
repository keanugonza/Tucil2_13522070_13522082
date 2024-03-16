import numpy as np

def pascal_triangle(n):
    triangle = [[0] * (n + 1) for _ in range(n + 1)]
    for line in range(n + 1):
        for i in range(line + 1):
            if i == 0 or i == line:
                triangle[line][i] = 1
            else:
                triangle[line][i] = triangle[line - 1][i - 1] + triangle[line - 1][i]
    return triangle

def pascal_function(n, t):
    triangle = pascal_triangle(n)
    result = []
    for i in range(n + 1):
        coeff = triangle[n][i] * ((1 - t) ** (n - i)) * (t ** i)
        result.append(coeff)
    return result

def bezier_pascal(points, iteration):
    precision = 1.0/2**iteration
    points_fix = []  
    t = 0
    n = len(points) - 1
    while t <= 1:
        pascal_coefficients = pascal_function(n, t)
        x = np.sum([coeff * point[0] for coeff, point in zip(pascal_coefficients, points)])
        y = np.sum([coeff * point[1] for coeff, point in zip(pascal_coefficients, points)])
        points_fix.append((x, y))  
        t += precision
    return points_fix
import matplotlib.pyplot as plt
import numpy as np
import time

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

# Algoritma Brute Force
def bezier_bf(points, iterations, precision=0.02):
    points_fix = [points[0]]
    t = 0
    while t <= 1:
        x = (1 - t)**2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t**2 * points[2][0]
        y = (1 - t)**2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t**2 * points[2][1]
        t += precision
        points_fix.append((x, y))
    points_fix.append(points[2])
    return points_fix 

# Menggunakan kakas matplotlib untuk visualisasinya
def plot_curve(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, marker='o')
    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Input
n = int(input("Masukkan banyaknya titik: "))
points = [tuple(map(float, input(f"Masukkan koordinat titik P{i} (pisahkan dengan spasi): ").split())) for i in range(n)]
iterations = int(input("Masukkan jumlah iterasi: "))

# Divide and conquer Execution Time
start_time = time.time()
curve_points_dc = bezier_dnc(n, points, iterations)
print(curve_points_dc)
end_time = time.time()
print("Divide and Conquer Approach Time:", end_time - start_time , "ms")

# Brute force Execution Time
start_time = time.time()
curve_points_bf = bezier_bf(points, iterations)
print(curve_points_bf)
end_time = time.time()
print("Brute Force Approach Time:", end_time - start_time, "ms")

# Visualisasi Kurva
plot_curve(curve_points_dc)
plot_curve(curve_points_bf)
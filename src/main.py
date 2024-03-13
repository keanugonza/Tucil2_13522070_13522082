from lib.Visualizer import plot_curve
import lib.DivideAndConquer as dnc
import lib.DivideWithClass as dnc2
import lib.BruteForce as bf
import time
import numpy as np
import os
import matplotlib.pyplot as plt

# Input
n = int(input("Masukkan banyaknya titik: "))
points = [tuple(map(float, input(f"Masukkan koordinat titik P{i} (pisahkan dengan spasi): ").split())) for i in range(n)]
iterations = int(input("Masukkan jumlah iterasi: "))

# Divide and conquer Execution Time
start_time = time.time()
curve_points_dc = dnc.bezier_dnc(n, points, iterations)
end_time = time.time()
# print(curve_points_dc)
print("Divide and Conquer Approach Time:", end_time - start_time , "ms")


# Divide and conquer Execution Time
bezier = dnc2.DevideAndConquer()
start_time = time.time()
bezier.create_bezier(points[0], points[1], points[2], iterations)
end_time = time.time()
# print(curve_points_dc)
print("Divide and Conquer Approach Time:", end_time - start_time , "ms")

# Brute force Execution Time
start_time = time.time()
curve_points_bf = bf.bezier_bf(points, iterations)
end_time = time.time()
# print(curve_points_bf)
print("Brute Force Approach Time:", end_time - start_time, "ms")

# Visualisasi Kurva
x_dc = [p[0] for p in curve_points_dc]
y_dc = [p[1] for p in curve_points_dc]
plot_curve(x_dc, y_dc, points)

plot_curve(bezier.resultPointsX,bezier.resultPointsY,points)

x_bf = [p[0] for p in curve_points_bf]
y_bf = [p[1] for p in curve_points_bf]
plot_curve(x_bf, y_bf, points)
from lib.Visualizer import plot_curve
import lib.DivideAndConquer as dnc
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
print(curve_points_dc)
end_time = time.time()
print("Divide and Conquer Approach Time:", end_time - start_time , "ms")

# Brute force Execution Time
start_time = time.time()
curve_points_bf = bf.bezier_bf(points)
print(curve_points_bf)
end_time = time.time()
print("Brute Force Approach Time:", end_time - start_time, "ms")

# Visualisasi Kurva
plot_curve(curve_points_dc)
plot_curve(curve_points_bf)
from lib.Visualizer import plot_curve
import lib.DivideAndConquer as dnc
import lib.DivideAndConquerBonus as dnc_bonus
import lib.BruteForce as bf
import lib.BruteForceBonus as bf_bonus
import lib.InputHandler as ih
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Get Input
n, points, iterations = ih.get_points()


if (n == 3):
    # Divide and conquer Execution Time
    bezier_dnc = dnc.DivideAndConquer()
    start_time = time.time()
    bezier_dnc.create_bezier(points, iterations)
    end_time = time.time()
    print("Divide and Conquer Approach Time:", end_time - start_time , "ms")

    # Brute force Execution Time
    start_time = time.time()
    curve_points_bf = bf.bezier_bf(points, iterations)
    end_time = time.time()
    print("Brute Force Approach Time:", end_time - start_time, "ms")

    curve_points_dnc = []
    for i in range(len(bezier_dnc.resultPointsX)):
        temp = (bezier_dnc.resultPointsX[i], bezier_dnc.resultPointsY[i])
        curve_points_dnc.append(temp)

    #Visualisasi kurva
    plot_curve(curve_points_dnc, points, "Divide and Conquer",iterations)
    plot_curve(curve_points_bf, points, "Brute Force",iterations)


else:
    # Divide and conquer Execution Time
    bezier_dnc = dnc_bonus.DivideAndConquerBonus()
    start_time = time.time()
    bezier_dnc.create_bezier(points, iterations)
    end_time = time.time()
    print("Divide and Conquer Approach Time:", end_time - start_time , "ms")

    # Brute force Execution Time
    start_time = time.time()
    curve_points_bf = bf_bonus.bezier_pascal(points, iterations)
    end_time = time.time()
    print("Brute Force Approach Time:", end_time - start_time, "ms")

    #Visualisasi kurva
    plot_curve(bezier_dnc.resultPoints, points, "Divide and Conquer",iterations)
    plot_curve(curve_points_bf, points, "Brute Force",iterations)
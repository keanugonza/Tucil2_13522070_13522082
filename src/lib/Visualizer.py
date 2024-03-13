import matplotlib.pyplot as plt
import numpy
from mpl_toolkits import mplot3d

# Menggunakan kakas matplotlib untuk visualisasinya
def plot_curve(curve_points, points):
    x = [p[0] for p in curve_points]
    y = [p[1] for p in curve_points]
    plt.plot(x, y, marker='o')
    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.plot(points[0][0], points[0][1], marker = 'o', markerfacecolor = 'red')
    plt.plot(points[1][0], points[1][1], marker = 'o', markerfacecolor = 'red')
    plt.plot(points[2][0], points[2][1], marker = 'o', markerfacecolor = 'red')
    plt.show()
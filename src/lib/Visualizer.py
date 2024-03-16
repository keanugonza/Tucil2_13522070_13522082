import matplotlib.pyplot as plt
import numpy
from mpl_toolkits import mplot3d

# Menggunakan kakas matplotlib untuk visualisasinya
def plot_curve(x, y, points):
    plt.plot(x, y, marker = "o")
    plt.title('Bézier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    for i in range (len(points)):
        plt.plot(points[i][0], points[i][1], marker = 'o', markerfacecolor = 'red')
    plt.show()
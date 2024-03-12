import matplotlib.pyplot as plt
import numpy
from mpl_toolkits import mplot3d

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
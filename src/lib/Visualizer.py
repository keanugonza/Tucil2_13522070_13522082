import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation


# Menggunakan kakas matplotlib untuk visualisasinya
def plot_curve(result, points, title):
    x = [p[0] for p in result]
    y = [p[1] for p in result]
    plt.title(f"Bézier Curve {title}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.plot(x, y, marker='.', markerfacecolor='blue')

    xp = [p[0] for p in points]
    yp = [p[1] for p in points]
    plt.plot(xp,yp, marker = "o", markerfacecolor = 'red')
    plt.show()
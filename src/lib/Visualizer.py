import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Menggunakan kakas matplotlib untuk visualisasinya
def plot_curve(result, points, title,i):
    x = [p[0] for p in result]
    y = [p[1] for p in result]
    plt.title(f"Bézier Curve {title}\n Iteration {i}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.plot(x, y, marker='.', markerfacecolor = "blue")
    xp = [p[0] for p in points]
    yp = [p[1] for p in points]
    plt.plot(xp,yp, marker = "o", markerfacecolor = 'red')
    plt.show()

# Menggunakan kakas matplotlib untuk visualisasi animasi titik per titik pada GUI
def animate_curve(results, points, title):
    fig, ax = plt.subplots()
    scat = ax.scatter([], [], s=5)
    line, = ax.plot([], [])
    xp = [p[0] for p in points]
    yp = [p[1] for p in points]
    plt.plot(xp,yp, marker = "o", markerfacecolor = 'red')
    # Mendapatkan ukuran yang sesuai untuk ukuran kurvanya 
    all_x = [x[0] for x in results + points]
    all_y = [x[1] for x in results + points]
    rentangX = max(all_x) - min(all_x)
    rentangY = max(all_y) - min(all_y)
    min_x, max_x = (min(all_x) - (0.1*rentangX)), (max(all_x) + (0.1*rentangX))
    min_y, max_y = (min(all_y) - (0.1*rentangY)), (max(all_y) + (0.1*rentangY))
    ax.set(xlim=[min_x, max_x], 
           ylim=[min_y, max_y], 
           xlabel='X', 
           ylabel='Y', 
           title=f"Bézier Curve {title}")
    ax.legend()

    # Animasi update
    def update(frame):
        x = [p[0] for p in results[:frame]]
        y = [p[1] for p in results[:frame]]
        data = np.stack([x, y]).T
        scat.set_offsets(data)
        line.set_xdata(x)
        line.set_ydata(y)
        return scat, line

    # Membuat animasi
    ani = animation.FuncAnimation(fig, update, frames=len(results) + 1, interval=100)
    plt.show()
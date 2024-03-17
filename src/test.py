import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

fig, ax = plt.subplots()
poin = [(0.0, 0.0), (19.140625, 60.546875), (39.0625, 117.1875), (59.765625, 169.921875), (81.25, 218.75), (103.515625, 263.671875), (126.5625, 304.6875), (150.390625, 341.796875), (175.0, 375.0), (200.390625, 404.296875), (226.5625, 429.6875), (253.515625, 451.171875), (281.25, 468.75), (309.765625, 482.421875), (339.0625, 492.1875), (369.140625, 498.046875), (400.0, 500.0), (431.640625, 498.046875), (464.0625, 492.1875), (497.265625, 482.421875), (531.25, 468.75), (566.015625, 451.171875), (601.5625, 429.6875), (637.890625, 404.296875), (675.0, 375.0), (712.890625, 341.796875), (751.5625, 304.6875), (791.015625, 263.671875), (831.25, 218.75), (872.265625, 169.921875), (914.0625, 117.1875), (956.640625, 60.546875), (1000.0, 0.0)]
xp = [p[0] for p in poin]
yp = [p[1] for p in poin]
scat = ax.scatter(xp, yp, s=5)
line = ax.plot(xp, yp)[0]
ax.set(xlim=[min(xp) -10, max(xp)+ 10], ylim=[min(yp) -10, max(yp)+ 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = xp[:frame]
    y = yp[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line.set_xdata(xp[:frame])
    line.set_ydata(yp[:frame])
    return (scat, line)


test = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
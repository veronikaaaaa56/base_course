import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

phi = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
line, = ax.plot([], [])


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')


def update(t):
    r = 0.5 * t
    line.set_data(r * np.cos(phi), r * np.sin(phi))
    return line,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 50))
ani.save('circle_animation.gif', writer='pillow', fps=20)
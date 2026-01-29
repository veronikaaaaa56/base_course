import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 4 * np.pi, 400)
x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
y = 12 * np.sin(t) + 8 * np.sin(1.5 * t)

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(-10, 50)
ax.set_ylim(10, 70) 

def update(a):
    X = 20 + x * np.cos(a) - y * np.cos(a)
    Y = 40 + y * np.cos(a) + x * np.sin(a)
    line.set_data(X, Y)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100), interval=30)
ani.save('dzdop3_animation.gif', writer='pillow', fps=20)
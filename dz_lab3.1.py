import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 12 * np.pi, 1000)
fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], color='purple', lw=10)


ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)


def update(frame):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5)

    line.set_data(x, y)
    return line, 

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 60), 
                    interval=30, blit=True)
ani.save('butterfly_animation.gif', writer='pillow', fps=20)
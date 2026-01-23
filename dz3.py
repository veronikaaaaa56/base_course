import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 2 * np.pi, 1000)
fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], color='red', lw=2)


ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)


def update(frame):
    s = 1 + 0.1 * np.sin(frame)
    
    x = s * (16 * np.sin(t)**3)
    y = s * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
    
    line.set_data(x, y)
    return line,

 
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 60), 
                    interval=30, blit=True)
ani.save('heart_animation.gif', writer='pillow', fps=20)
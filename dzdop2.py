import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
line1, = ax.plot([], [], 'r', lw=2) 
line2, = ax.plot([], [], 'b', lw=2) 

def update(t_end):
    t = np.linspace(0, t_end, 200)    
    line1.set_data(t, 1.0 * np.sin(2 * t))
    line2.set_data(t, 0.5 * np.sin(5 * t))
    return line1, line2

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), blit=True, interval=30)
ani.save('dzdop2_animation.gif', writer='pillow', fps=20)
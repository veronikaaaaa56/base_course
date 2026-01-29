import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

a = 5  
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-a, a)
ax.set_ylim(-a, a)
ax.axis('off') 

line, = ax.plot([], [], 'b-', lw=2)


square = np.array([[-a/2, -a/2], [a/2, -a/2], [a/2, a/2], [-a/2, a/2], [-a/2, -a/2]])

def update(angle):
    theta = np.radians(angle)
  
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated = square @ R.T
    line.set_data(rotated[:, 0], rotated[:, 1])
    return line,


ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 10), interval=50)
ani.save('dzdop4_animation.gif', writer='pillow', fps=20)
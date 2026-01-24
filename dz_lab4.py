import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x0 = [0.1]
y0 = [0.1]
C = 0.3
D = 0.33

for _ in range(500):
    x0.append (x0[-1]**2 - y0[-1]**2 + C)
    y0.append (2 * x0[-2] * y0[-1] + D)

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
plt.axis('equal')
point, = ax.plot([], [], 'pink')

def update(i):
    point.set_data(x0[:i], y0[:i])
    return point, 

ani = FuncAnimation(fig, update, frames=500 , interval=20)
ani.save('points.1_animation.gif', writer='pillow', fps=20)


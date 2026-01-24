import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 4 * np.pi, 1000)

x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
y = 12 * np.sin(t) + 8 * np.sim(1.5 * t)

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
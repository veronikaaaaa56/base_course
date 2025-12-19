import numpy as np
import matplotlib.pyplot as plt 

def draw_ladder(num_steps):

    x_values = np.linspace(0, num_steps, num_steps * 100 + 1)

    y_values = np.floor(x_values)

    plt.step(x_values, where = 'post', color = 'red')
    plt.xlabel('X - ось')
    plt.ylabel('Y - ось (Значение N)')


draw_ladder(5)

plt.savefig(dz_lab4dop.png)
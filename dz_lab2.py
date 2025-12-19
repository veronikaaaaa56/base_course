import numpy as np
import matplotlib.pyplot as plt 

def hyperbola(x_start, x_end, N):


    x = np.linspace(x_start, x_end, N)
    k = 1
    y = k / x

    plt.plot(x, y, label=f'y = {k / x}')
    plt.xlabel('X - ось')
    plt.tlabel('Y - ось')


hyperbola(0.1, 10, 100)

plt.savefig('dz_lab2.png')
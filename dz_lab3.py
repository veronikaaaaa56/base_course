import numpy as np
import matplotlib.pyplot as plt 

def plot_ellips(start_angel, end_angel, N):

    h, k = 0, 0
    a = 5
    b = 3


    t = np.linspace(start_angel, end_angel, N)


    x = h + a * np.cos(t)
    y = k + b * np.sin(t)

    
    plt.plot(x, y, color='pink')
    plt.xlabel('X - ось')
    plt.ylabel('Y - ось')


plot_ellips(0, 2 * np.pi, 100)

plt.savefig('dz_lab3.png')
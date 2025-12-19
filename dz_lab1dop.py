import numpy as np
import matplotlib.pyplot as plt 

def lissajous(a, b, A=1, B=1, delta=np.pi/2 ):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)


    plt.plot(x, y, color='purple')
    plt.xlabel('X')
    plt.ylabel('Y')


lissajous(a=1, b=1, A=1, B=1)

plt.savefig('dz_lab1dop.png')
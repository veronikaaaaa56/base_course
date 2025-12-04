import numpy as np

def x_y(a, b, N):
    x = np.linspace(a, b, N)
    y = x**2
    return y


print(x_y(2, 5, 7))
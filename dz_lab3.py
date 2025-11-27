import numpy as np

g = 9.8 

x_0 = 2
y_0 = 5
v = 16
alpha = np.pi / 180 * 45
vx_0= v * np.cos(alpha)
vy_0= v * np.sin(alpha)

coords = []
for t in np.arange (0, 5, 0.1):
    x = x_0 + vx_0 * t 
    y = y_0 + vy_0 * t - g * t**2 / 2

    coords.append([t, x , y])

coords = np.array(coords)
print(coords)

print()

t = np.arange(0, 5,)
x = x_0 + vx_0 * t 
y = y_0 + vy_0 * t - g * t**2/2

coords = np.zeros((len(t), 3))
coords[:, 0] = t
coords[:, 1] = x
coords[:, 2] = y
print(coords)

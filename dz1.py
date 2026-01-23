import numpy as np
import matplotlib.pyplot as plt

R = 1  
t = np.linspace(0, 4 * np.pi, 1000)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

plt.figure(figsize=(10, 4))
plt.plot(x, y, color='blue')
plt.savefig('DZ1.png')

plt.close()


R = 5
t = np.linspace(0, 2 * np.pi, 1000)

x = R * np.cos(t)**3
y = R * np.sin(t)**3

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.savefig('DZ1,1.png')
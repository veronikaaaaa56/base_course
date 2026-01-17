import matplotlib.pyplot as plt
import numpy as np

R = 1
t = np.linplace(0,2 * np.pi, 1000)

x = R * (t - np.sin(t))
y = R * (t - np.cos(t))

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax (x, y, '-')
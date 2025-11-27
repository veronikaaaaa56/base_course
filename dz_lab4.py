import numpy as np
from math import sin
N = 5
M = 6

trigonometry_array = np.zeros((N, M))
for i in range (N):
    for j in range (M):
        trigonometry_array[i, j] = sin(N * i + M * j + 1)

for i in range(N): 
    for j in range(M):
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0 

print(trigonometry_array)


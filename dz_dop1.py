import numpy as np 

a = [
    [2, 3, 1, 4, 5, 6, 7]
    [8, 1, 3, 2, 2, 6, 8]
    [1, 4, 3, 1, 0, 2, 5]
    [4, 5, 0, 1, 3, 2, 1]
    [8, 7, 9, 1, 0, 2, 3]
]

slice = a[0:3:, 0:2]
print(slice)

slice = a[0:3: , 5:6]
print(slice)

slice = a[1:3:, 3:5]
print(slice)

slice= a[3:: , 2:4]
print(slice)

slice = a[4:: , 0:2]
print(slice)

slice = a[3:4:, 5::]
print(slice)
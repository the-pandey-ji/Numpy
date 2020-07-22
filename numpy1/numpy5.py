import numpy as np

# SLICING
arr = np.arange(1, 101).reshape(10, 10)
print(arr)
print(arr[0, 0])

print(arr[1])
print("new")
print(arr[0:3:2, 2:6:2])

print(arr[::])
print(arr[:])
print(arr[:, :])

print(arr.itemsize)

print(arr[:, 4].ndim)

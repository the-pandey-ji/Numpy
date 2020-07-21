# mathematic operations using numpy
import numpy as np
arr=np.arange(1,10)
print(arr)
arr2=arr.reshape(3,3)
arr3=np.arange(1,10).reshape(3,3)
print(arr2)
#  Addition
print(arr2+arr3)
print(np.add(arr2,arr3))

# Subtraction
print(arr2-arr3)
print(np.subtract(arr2,arr3))



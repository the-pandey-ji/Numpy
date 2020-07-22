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

# Divide
print(arr2/arr3)
print(np.divide(arr2,arr3))

# Remainder
print(arr2%arr3)

# Multiply
print(arr2*arr3)
print(np.multiply(arr2,arr3))

# matrix product
print(arr2@arr3)
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
print(np.dot(arr2,arr3))

# max
print(arr2.max())
# 9
# max element's index
print(arr2.argmax())
# 8
# max value in all columns
print(arr2.max(axis=0))
# max value in all row
print(arr2.max(axis=1))

# index of max values
print(arr2.argmax(axis=0))

# min
print(arr2.min())

# min element's index
print(arr2.argmin())

# min value in all columns
print(arr2.min(axis=0))
# min value in all row
print(arr2.min(axis=1))

# index of min values
print(arr2.argmin(axis=0))


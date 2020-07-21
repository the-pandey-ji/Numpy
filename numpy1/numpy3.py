import numpy as np
# arange
arr=np.arange(1,13)
print(arr)

print(np.arange(1,20,2))

# linespace
print(np.linspace(0,20,5))

# reshape
print(np.ones(12).reshape(3,2,2))
arr2=np.ones(12).reshape(3,4)
print(arr2.reshape(12))

# ravel function
print(arr2)
print(arr2.ravel())

# flatten function
print("flatten function")
print(arr2.flatten())

# CONCATENATION AND SPLIT
import numpy as np

arr1 = np.arange(1,26).reshape(5,5)
arr2 = np.arange(26,51).reshape(5,5)


print(arr1)
print(arr2)

# concatenate
# colum wise
print(np.concatenate((arr1,arr2)))
print(np.vstack((arr1,arr2))) # np.vsatck
# row wise
print(np.concatenate((arr1,arr2),axis=1))
print(np.hstack((arr1,arr2)))

print(np.hstack((arr1,arr2,arr1)))

# split

list1=np.split(arr1,5)
print(list1)
print(list1[0])

# split row wise
print(np.split(arr1,5,axis=1))

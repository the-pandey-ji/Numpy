import numpy as np
import random
print("random  numbers in a range")
print(np.random.random((2,3)))

print("random number in a range")
print(np.random.randint(1,100,(5,5)))
np.random.seed(1)
arr=np.random.randn(5)
print(arr)
print("print same random values using seed values")
np.random.seed(1)
print(np.random.randn(5))

print("choose random values from a list or array")
li=np.array([1213,24,35,46,7575,57,75])
print(np.random.choice(li,(2,2)))

for i in range(10):
    print(np.random.permutation(li))

# TROGONOMETRY
import numpy as np
# matplotlib.pyplot for graphs
import matplotlib.pyplot as plt

print(np.sin(np.pi / 2))
print(np.cos(180))
print(np.tan(120))
print("finish")

arr = np.arange(0, 3 * np.pi, .1)
arr1 = np.sin(arr)
print("""arr=np.linspace(0, 3 * np.pi,20).reshape(4,5)""")
print(arr)
print(arr1)

plt.plot(arr, arr1)
plt.show()

cos_y=np.cos(arr)

plt.plot(arr,cos_y)
plt.show()

import numpy as np

a = np.array([[(1,2,3,6),(4,5,6,8)]])
print(a[0][1][2])
print(a)
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.shape)
#print(a.shape)

# reshape

a = np.array([(1,2,3,4,5,6),(4,5,6,7,8,9)])
print(a)
a= a.reshape(6,2)
print(a)

#slicing
a = np.array([(1,2,3,4,5,6),(1,2,3,4,5,6)])
print(a)

print(a[:,3])
print(a[0:2,4])

# linspace
a= np.linspace(1,3,5)
print(a)

a= np.linspace(20,40,11)
print(a)
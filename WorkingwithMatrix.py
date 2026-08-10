from numpy import *

arr1=array([
    [1,2,3,6,5,7],
    [4,5,6,11,23,42]
])

print(arr1)

print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)
print(arr1.size)

arr2=arr1.flatten()

arr3=arr2.reshape(2,2,3)

print(arr3)


m=matrix('1,2,3;6,4,5;1,6,7')

print(m.max())
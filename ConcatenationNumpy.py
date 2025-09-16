import numpy as np
arr1=np.array(([20,15,60],[87,65,54]))
arr2=np.array(([23,45,67],[34,22,13]))
print(np.concatenate([arr1,arr2]))

print(np.concatenate([arr1,arr2],axis=1))

b=np.array_split(arr1,2)


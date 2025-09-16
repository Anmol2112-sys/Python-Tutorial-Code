import numpy as np
arr=np.array([[65,45,23,22,11],[2,7,5,1,3]])
print(np.sort(arr))


arr=np.array([3,4,1,8,7])
s=np.where(arr%2==0)
print(s)


fa=arr>35

new=arr[fa]
print(new)
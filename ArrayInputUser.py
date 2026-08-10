from array import *
arr=array('i',[])

n=int(input("Enter the number of elements: "))
for i in range(n):
    x=int(input("Enter the next value:"))
    arr.append(x)


    print(arr)


    val=int(input("Enter the value to be searched:"))
      

    k=0
    for i in arr:
        if i==val:
            print("Value found")
            break 
        k+=1
pos = -1


def search(list,n):
    i=0

    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            pos=i
            print("Found at index",i)
            return True
        i+=1
        
    return False


list=[5,8,9,2,4,6]
n=4

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
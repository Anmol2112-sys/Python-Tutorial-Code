from array import *

vals= array('i',[5,10,15,20])


for i in range(3):
    print (vals[i])

newArr=array(vals.typecode,(a for a in vals))

for e in newArr:
    print(e)

i=0
while i<len(newArr):
    print(newArr[i])
    i+=1


print(vals)
vals.reverse()
print(vals)

print(vals.buffer_info())
print(vals.typecode)


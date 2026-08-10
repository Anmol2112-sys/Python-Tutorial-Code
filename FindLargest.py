lis=[4,56,78,21,11]
largest=lis[0]
for i in range(1,len(lis)):
    if lis[i]>largest:
        largest=lis[i]

print("The largest number in the list is:",largest)

from functools import reduce

nums=[3,2,4,6,7,8,99,0]

evens=list(filter(lambda n:n%2==0,nums))

dpoubles=list(map(lambda n:n*2,evens))

sum=reduce(lambda a,b:a+b,dpoubles)

print(evens)
print(dpoubles)
print(sum)
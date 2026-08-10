#f=open('Multithreading.py','r')
#print(f.read())
#print(f.readline())

f1=open('abc','w')
f1.write("Something")
f1.write('People')

for data in f1:
    f1.write(data)

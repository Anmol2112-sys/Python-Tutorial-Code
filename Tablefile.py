file=open("Table.txt","w")
a=int(input("Enter a number: "))
file.write(f"Multiplication Table of {a}\n")
for i in range(1,11):
    file.write(f"{a} x {i} = {a*i}\n")
file.close()
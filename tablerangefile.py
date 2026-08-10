
user1=int(input("Enter a number:"))
user2=int (input("Enter another number:"))
file=open("table.txt","w")
file.write(f"Multiplication Table of {user1} to {user2}\n")
for i in range(user1,user2+1):
    for j in range(1,11):
        file.write(f"{i} x {j} = {i*j}\n")
    file.write("\n")
file.close()

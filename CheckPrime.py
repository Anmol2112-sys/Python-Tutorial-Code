
num=int(input("Enter a number here:"))
if num<=1:
    print("It is not prime.")
else:
    for i in range (2,num):
        if num%i == 0:
            print("Number is not prime.")
            break
        else:
         print("It is a prime number.")
         break
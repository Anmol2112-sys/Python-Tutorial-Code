num=int(input("Enter a number:"))
temp=num
rev=0
while (num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10

if (rev==temp):
    print("It is palindrome")
else:
    print("It is not palindrome.")
            
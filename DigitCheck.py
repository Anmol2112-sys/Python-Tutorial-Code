number=int(input("Enter a number:"))
if number>=0 and number<= 9:
    print("Single digit number")
elif number >= 10 and number<= 99:
    print("Double digit number")
elif number>= 100 and number<= 999:
    print("Three digit number")
elif number>= 1000 and number<= 9999:
    print("Four digit number")
else:
    print("Number is greater than four digits")
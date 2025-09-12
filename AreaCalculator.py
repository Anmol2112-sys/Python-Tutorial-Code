print("****AREA CALCULATOR***" )
print("1.Area of Circle")
print("2.Area of Square")
print("3.Area of Rectangle")
print("4.Area of Triangle")
choice = int(input("Enter your choice:"))
if choice==1:
    r=float(input("Enter the radius of circle:"))
    area=3.14*r*r
    print("Area of Circle is:",area)
elif choice==2:
    s=float(input("Enter the side of square:"))
    area=s*s
    print("Area of Square is:",area)
elif choice==3:
    l=float(input("Enter the length of rectangle:"))
    b=float(input("Enter the breadth of rectangle:"))
    area=l*b
    print("Area of Rectangle is:",area)
elif choice==4:
    b=float(input("Enter the base of triangle:"))
    h=float(input("Enter the height of triangle:"))
    area=0.5*b*h
    print("Area of Triangle is:",area)
else:
    print("Invalid choice")
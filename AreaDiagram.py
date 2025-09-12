print("****AREA CALCULATOR***" )
print("1.Area of Circle")
print("2.Area of Square")
print("3.Area of Rectangle")
print("4.Area of Triangle")
choice = int(input("Enter your choice:"))
if choice==1:
   while True:
    r=float(input("Enter the radius of circle:"))
    area=3.14*r*r
    print("Area of Circle is:",area)
    break
elif choice==2:
  while True:
    s=float(input("Enter the side of square:"))
    area=s*s
    print("Area of Square is:",area)
    break
elif choice==3:
        while True:
          l=float(input("Enter the length of rectangle:"))
          b=float(input("Enter the breadth of rectangle:"))
          area=l*b
          print("Area of Rectangle is:",area)
          break
elif choice==4:
    while True:
              b=float(input("Enter the base of triangle:"))
              h=float(input("Enter the height of triangle:"))
              area=0.5*b*h
              print("Area of Triangle is:",area)
              break
else:
   while True:    
           print("Invalid choice")
           break
while True:
    name=input("Enter customer name:")
    total=0
    while True:
        print("Enter the amount and quantity:")
        amount=float(input("Enter amount:"))
        quantity=float(input("Enter quantity:"))
        total=total+amount *quantity
        repeat=input("Do you want to add more items?(yes/no):")
        if repeat=="no" or repeat=="No":
            break
        print("-"*40)
        print("Name:",name)
        print("Amount to be paid:",total)
        print("-"*40)
        print("********Happy Shopping**********")
        repeat1= input("Do you want to go to next customer ?(yes/no):")
        if repeat1== "no" or repeat=="NO":
            break
def check_prime(num):
    if num==1:
        print("It is not a prime number")
    if num==2:
        print("It is a prime number")
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number")
            break

    else:
        print("It is a prime number")


check_prime(11)
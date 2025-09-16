def add(numbers):
    total=0
    for i in numbers:
        total=total+i
    return(total)

print("The sum of all items in the list",add([12,4,5,13,23]))
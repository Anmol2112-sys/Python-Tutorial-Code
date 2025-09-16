def max(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
    
print(max(12,16,65))
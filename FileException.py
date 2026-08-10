
a=5
b=2


try:
    print("resource Open")
    print(a/b)
    
except Exception as e:
    print("An Error Occurred",e)

except ValueError as e:
    print("invalid input")

except Exception as e:
    print("Something went Wrong...")
    

   

finally:
    print("resource Closed")

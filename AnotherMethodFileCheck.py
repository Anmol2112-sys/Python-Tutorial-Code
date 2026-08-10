a=input("enter the file name")
b=a.split(".txt")
print(b)
if(a.endswith(".txt")):
    print("file is text file")
elif(a.endswith(".py")):
    print("file is python file")
elif(a.endswith(".java")):
    print("file is java file")
elif(a.endswith(".cpp")):
    print("file is c++ file")
else:
    print("file is not text,python,java or c++ file")
        
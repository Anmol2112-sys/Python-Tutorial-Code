a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="hello  123@"
g="1.234"
print(b,b.isalpha())
print(d,d.isupper())
print(f,f.islower())
print(e,e.isspace())
print(f,f.isspace())
print(d,d.istitle())

a="****Harry Potter...."
print(a,a.endswith("r"))
print(a,a.startswith("P",6,9))
print(a.swapcase())
print(a.strip("*,"))
a="OOFD#BRB#OMW#TB"
print(a.split("#"))
a="Harry Potter"
x=a.rjust(20,"-")
print(x,"is my favorite movie")
a="my name is anmol"
print(a.replace("anmol","aadya"))
a="bibidy bobidy boo"
print(a.rindex("dy"))
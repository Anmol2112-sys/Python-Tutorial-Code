names=["Anmol","Navin","Aditya","Anmol"]
comps=("Rubrik","Apple","MS","Rubrik")

zipped=set(zip(names,comps))

for (a,b) in zipped:
    print(a,b)
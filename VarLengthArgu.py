def person(name,**data):
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)



person(name="Anmol Aditya",age=21,city="Jaipur",phone=98012096)
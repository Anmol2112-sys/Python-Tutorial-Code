class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()


    class Laptop:

        def __init__(self):
            self.brand="Asus"
            self.cpu="Ryzen7"
            self.ram=16



        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("Anmol",1)
s2=Student("Navin",3)

s1.show()






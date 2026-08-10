from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
       pass

class Whiteboard:
    def write(self):
        print("writing on whiteboard")
        

class Pc(Computer):
    def process(self):
        print("Solving Bugs")
    



com1=Pc()
com1.process()
prog1=Pc()


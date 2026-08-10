class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("in init method")



    def config(self):
        print("config is : ", self.cpu, self.ram)





com1 = Computer("i7", "16GB")
com2 = Computer("Ryzen 7", "32GB")

com1.config()
com2.config()

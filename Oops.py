class Computer:
  def config(self):
    print("Ryzen7,16gb,512gb,Asus Vivobook")
class Mobile:
    def config(self):
        print("Snapdragon 888,8gb,128gb,OnePlus Nord")
a=5.5
com1=Computer()
print(type(a))
print(type(com1))

Computer.config(com1)
Mobile.config(Mobile())
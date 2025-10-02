import matplotlib.pyplot as plt 
days=[1,2,3,4,5,6,7,8]
NOP1=[5,10,30,20,35,60,80,70]
NOP2=[10,20,30,40,50,60,55,65]
NOP3=[8,30,50,65,45,67,78,99]
plt.stackplot(days,NOP1,NOP2,NOP3)
plt.show()
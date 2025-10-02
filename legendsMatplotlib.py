import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[45,67,33,62,12]
y1=[41,60,13,66,13]
plt.figure(figsize=[4,6])
plt.plot(x,y,label="male")
plt.plot(x,y1,label="Female")
plt.legend(["a1","a2"])
plt.show()
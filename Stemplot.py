import matplotlib.pyplot as plt 
x=[23,34,45,20,30,40,43,50,55,60,65,67]
plt.stem(x,linefmt= "--",markerfmt="D",bottom=10,orientation='horizontal')
plt.show()
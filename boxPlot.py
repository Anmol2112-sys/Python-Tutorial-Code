import matplotlib.pyplot as plt 

l=[23,43,49,67,54,45,34,39]
plt.boxplot(l)
plt.savefig("bar.png")
plt.show()
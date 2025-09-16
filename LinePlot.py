import matplotlib.pyplot as plt


x=["Day1","Day2","Day3","Day4"]
y=[200,400,600,800]
y1=[452,321,234,678]
plt.plot(x,y,marker="^",ls="--",color="green",label="week1")
plt.plot(x,y1,marker="+",ls="-",color="blue",label="week2")
plt.legend()
plt.show()
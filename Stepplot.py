import matplotlib.pyplot as plt 
x=["day1","day2","day3","day4","day5"]
y=[30,40,50,60,65]
plt.step(x,y,where="post",marker="o")
plt.show()
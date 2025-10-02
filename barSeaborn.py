import seaborn as sns 
import matplotlib.pyplot as plt

data=sns.load_dataset("tips")
print(data)
sns.barplot(data=data,x="day",y="tip",palette="spring")
plt.plot()
plt.show()
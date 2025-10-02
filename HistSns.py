import seaborn as sns 
import matplotlib.pyplot as plt

data=sns.load_dataset('tips')
sns.histplot(data,x='day',hue="sex",kde="true")
print(data)
plt.show()
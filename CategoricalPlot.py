import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data=sns.load_dataset('tips')
print(data)

#categoricalPlot
sns.catplot(x="day",y="tip",data=data,hue="sex",kind="violin")
plt.show()
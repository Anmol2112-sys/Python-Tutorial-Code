import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

data=sns.load_dataset("tips")
print(data)

sns.swarmplot(data=data,x="day",y="total_bill",hue="sex",dodge=True)
plt.show()
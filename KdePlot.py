import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 


data=sns.load_dataset("tips")

sns.kdeplot(data=data,x="total_bill",hue="sex",multiple="stack")
plt.show()
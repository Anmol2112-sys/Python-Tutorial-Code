import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data=sns.load_dataset('tips')

sns.stripplot(data=data,x='day',y='total_bill', hue='sex',dodge=True)
plt.show()
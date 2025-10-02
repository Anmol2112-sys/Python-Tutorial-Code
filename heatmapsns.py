import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

data=sns.load_dataset('tips')
print(data)

sns.heatmap(data=data,x='total_bill',y='tip')
plt.show()

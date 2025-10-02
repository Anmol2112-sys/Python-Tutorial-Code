import seaborn as sns 
import matplotlib.pylab as plt 
import pandas as pd

data=sns.load_dataset('tips')
print(data)
sns.scatterplot(data=data,x='total_bill',y='tip',hue="smoker")
plt.show()
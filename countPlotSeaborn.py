import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

data=sns.load_dataset("tips")
print(data)

sns.countplot(data=data,x="department")
plt.show()
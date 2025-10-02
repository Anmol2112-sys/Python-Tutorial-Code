import seaborn as sns 
import matplotlib.pyplot as plt 

data=sns.load_dataset("tips")

sns.relplot(data,x="tip",y="total_bill",hue="sex",kind="line")
plt.show()
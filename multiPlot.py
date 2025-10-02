import seaborn as sns 
import matplotlib.pyplot as plt 

data=sns.load_dataset('tips')
print(data)

a=sns.FacetGrid(data,col="smoker",height=2)
a.map(sns.barplot, "day","tip")
plt.show()
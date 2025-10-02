import matplotlib.pyplot as plt 
import seaborn as sns 

data=sns.load_dataset("exercise")
sns.set_style(style="dark")
sns.barplot(x="time",y="pulse",data=data)

sns.palplot(sns.color_palette("viridis"))
plt.show()


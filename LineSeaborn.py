import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

data=pd.read_excel("c:/Users/anmol/Desktop/InsuranceDashboard.xlsx")
sns.lineplot(data=data ,x="charges",y="region")
plt.show()
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_excel("c:/Users/anmol/Desktop/InsuranceDashboard.xlsx")
df=pd.DataFrame(data)
print(df)
grouped_by=df.groupby("region")["charges"].sum()
print(grouped_by)
plt.bar(grouped_by.index,grouped_by.values)
plt.show()
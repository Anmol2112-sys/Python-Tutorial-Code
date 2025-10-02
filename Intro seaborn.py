import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 
data={"days":[1,2,3,4,5,],
      "NOP":[50,60,70,54,44]}
df=pd.DataFrame(data)
print(df)

sns.lineplot(data=data,x="days",y="NOP")
plt.show()

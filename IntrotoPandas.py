import pandas as pd
import numpy as np

data=pd.read_excel("c:\\Users\\anmol\\Desktop\\InsuranceDashboard.xlsx")
print(data)
print(data.isnull())
 
data["age"]=data["age"].replace(np.nan,44)
print(data)

print(data["age"].mean())

print(data.fillna(method="bfill"))
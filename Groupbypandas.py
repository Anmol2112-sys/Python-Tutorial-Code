import pandas as pd
data=pd.read_excel("c:\\Users\\anmol\\Desktop\\InsuranceDashboard.xlsx")
print(data.head(10))

gp=data.groupby(["age"]).agg({"charges":"count"})
print(gp)

gp1=data.groupby(["region"]).agg({"age":"mean"})
print(gp1)


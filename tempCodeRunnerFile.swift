import pandas as pd

data=pd.read_excel("c:\\Users\\anmol\\Desktop\\InsuranceDashboard.xlsx")
print(data)

data.loc[(df["charges %"]==0),"GetsBonus"]="no bonus"
data.loc[(df["charges %"]>0),"GetsBonus"]=" bonus"
print(data.head())


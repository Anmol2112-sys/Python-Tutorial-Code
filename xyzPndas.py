import pandas as pd


data=pd.read_excel("c:\\Users\\anmol\\Desktop\\InsuranceDashboard.xlsx")
print(data)


print(data.head())

data={"Months":["January","February","March","April"]}
a=pd.Dataframe(data)
print(a)

def extract(value):
    return value[0:3]

a["Short_months"]=a["Months"].map(extract)
print(a)
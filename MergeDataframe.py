import pandas as pd
data1={"Emp Id":["E01","E02","E03","E04"],
       "Names":["Ram","Shyam","Rahul","Vishal"],
       "Age":[23,24,34,46]}

data2={"Emp Id":["E01","E02","E03","E04"],
       "Salary":[45000,27000,35000,31000]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(df1)
print()
print(df2)


print(pd.merge(left=df1,right=df2,on="Emp Id",how="left"))


data1={"Emp Id":["E06","E07","E08","E09"],
       "Names":["Golu","Anmol","Ravi","Bholu"],
       "Age":[23,24,34,46]}

data2={"Emp Id":["E06","E07","E08","E09"],
       "Salary":[50000,70000,40000,90000]}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(pd.concat([df1,df2]))
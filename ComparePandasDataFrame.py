import pandas as pd 
dict={"Fruits":["Mango","Apples","Banana","Papaya"],
      "Price":[100,150,50,45],
      "Qunatity":[15,10,10,3]}

df1=pd.DataFrame(dict)
print(df1)
df2=df1.copy()

df2.loc[0,"Price"]=120
df2.loc[1,"Price"]=90
df2.loc[3,"Price"]=112
df2.loc[1,"Price"]=190
df2.loc[0,"Price"]=170
df2.loc[3,"Price"]=156

print(df2)
print(df1.compare(df2))
print(df1.compare(df2,keep_equal=True))
print(df1.compare(df2,keep_shape=True))
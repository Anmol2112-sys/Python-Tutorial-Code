import pandas as pd 
dict={"Keys":["K1","k2","K3","K4"],
       "Names":["John","Anmol","Peter","Lisa"],
        "Houses":["Red","Blue","Green","Yellow"]}

df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Keys"],value_vars=["Names"]))
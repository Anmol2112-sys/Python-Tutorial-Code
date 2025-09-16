import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

brands=["Oneplus","Nokia",'Redmi',"Samsung","Motorola"]
x=[25,45,20,30,35]
c=["red","orange","blue","green","yellow"]
ex=[0,0,0,0,1]
plt.pie(x,labels=brands,explode=ex,colors=c,shadow=True,autopct="%.2f")
plt.show()
""""
Este codigo calcula los retornos mensuales de las 3000 acciones en periodicidad mensual
para luego introducirlas al panel
"""

import pandas as pd
import os
print ("Se importaron las librerias necesarias")

n_stocks=3000

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_MENSUAL.xlsx")
df=pd.read_excel(path,sheetname="A")
print ("Se importo al dataframe")

df=df.set_index("Dates")

names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

print ("Modificando el tamano del dataframe")
#df2=df.iloc[:,0:3000]

print ("Calculando retornos")
df2=df.pct_change(periods=1)
#df2=1 - df / df.shift(1)
#df2=df.pct_change()[df.shift(1).notnull()].dropna()

df3=df2.stack()
path2=os.path.join("PROCESSED","RUSSELL_stacked.csv")
#df3.columns=["a","b","c"]
print ("Exportando matriz de correlacion a CSV")
df3.to_csv(path2,cols=["a","b","c"])

if __name__ == '__main__':
    print (df3)

"""
Este codigo toma el excel que lanza bloomberg con todos los activos y convierte el dataframe a
formato hdf, primer codigo en correr


"""

import pandas as pd
import os
print ("Se importaron las librerias necesarias")

indexes_1=["RUSSELL_3000.xlsx","SP_500.xlsx","FTSE_100.xlsx"]

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW",indexes_1[2])
df=pd.read_excel(path)
print ("Se importo al dataframe"+" "+indexes_1[2])



df=df.set_index("Dates")
names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

indexes_2=["RUSSELL_3000.hdf","SP_500.hdf","FTSE_100.hdf"]
path2=os.path.join("RAW",indexes_2[2])

# HDF
print ("Exportando la base HDF"+" "+ indexes_2[2])
df.to_hdf(path2,key="table",comp="blosc")
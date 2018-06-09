"""
Este codigo toma el excel que lanza bloomberg con todos los activos y convierte el dataframe a
formato hdf, primer codigo en correr


"""

import pandas as pd
import os
print ("Se importaron las librerias necesarias")



os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000.xlsx")
df=pd.read_excel(path)
print ("Se importo al dataframe")



df=df.set_index("Dates")
names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names


path2=os.path.join("RAW","RUSSELL_3000.hdf")

# HDF
print ("Exportando la base HDF")
df.to_hdf(path2,key="table",comp="blosc")
"""
Este codigo toma el hdf con los precios, calcula los retornos y
calcula una matriz de correlación 3000x3000, y la exporta en formato hdf y formato csv
No aplica ninguna transformación adicional a los datos

"""

import pandas as pd
import os
import numpy as np
print ("Se importaron las librerias necesarias")

n_stocks=3000
threshold=0.3

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000.hdf")


print ("Importando los datos")
df = pd.read_hdf(path, key='table')



names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

print ("Modificando el tamaño del dataframe")
df2=df.iloc[:,0:n_stocks]

print ("Calculando retornos")
df3=df2.pct_change(periods=1)

print ("Calculando la matriz de correlacion")
corr_matrix=df3.corr()
corr_matrix=corr_matrix.replace(float(1.0),np.nan)
corr_matrix[( corr_matrix>= -threshold) & (corr_matrix <= threshold)] = np.nan
#corr_matrix=corr_matrix.cut(corr_matrix.columns,bins=[-0.1,0.1],labe)
path2=os.path.join("RAW","CORR_MATRIX.csv")
path3=os.path.join("RAW","CORR_MATRIX.hdf")

# CSV y HDF
print ("Exportando matriz de correlación a CSV")
corr_matrix.to_csv(path2,header=names[:n_stocks],chunksize=100)
print ("Exportando matriz de correlación a HDF")
corr_matrix.to_hdf(path3,key='table', comp='blosc')


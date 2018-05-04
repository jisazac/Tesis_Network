"""
Este jupyter toma el excel que lanza bloomberg con todos los activos y su precios historicos,
calcula una matriz de correlación 3000x3000 y luego exporta la matriz de adyacencia en formato csv
usando ciertos criterios para definir el enlace


"""

import pandas as pd
import numpy as np
import os
print ("Se importaron las librerias necesarias")

n_stocks=3000
corr_cut=0.9

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000.xlsx")
df=pd.read_excel(path)
print ("Se importo al dataframe")


names=[]
df=df.set_index("Dates")

for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names


df2=df.iloc[:,0:n_stocks]

print ("Se modifico el tamaño del dataframe")

print ("Calculando la matriz de correlacion")
corr_matrix=df2.corr()
path2=os.path.join("RAW","RUSSELL_3000_corr.csv")

corr_matrix_positive=corr_matrix.replace(1,0)
corr_matrix_positive[corr_matrix_positive < corr_cut] = 0
corr_matrix_positive[corr_matrix_positive > 0] = 1

# CSV
print ("Exportando el archivo CSV")
corr_matrix_positive.to_csv(path2,header=names[:n_stocks],chunksize=100)
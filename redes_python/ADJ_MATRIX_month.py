"""
Este jupyter toma el hdf de la matriz de correlacion, calcula
una matriz de adjacencia con o sin pesos y la exporta a HDF
y csv


"""
from redes_python.utils import metrica_scalar
import pandas as pd
import os
print ("Se importaron las librerias necesarias")

n_stocks=3000
corr_cut=0.9

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","CORR_MATRIX.hdf")


print ("Importando los datos")
df = pd.read_hdf(path, key='table')


names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

print ("Modificando el tamaño del dataframe")
df2=df.iloc[:,0:n_stocks]


print ("Calculando Pesos")
adj_matrix=df2.applymap(metrica_scalar)


path2=os.path.join("RAW","ADJ_MATRIX.csv")
path3=os.path.join("RAW","ADJ_MATRIX.hdf")

# CSV y HDF
print ("Exportando matriz de adyacencia a CSV")
adj_matrix.to_csv(path2,header=names[:n_stocks],chunksize=100)
print ("Exportando matriz de adyacencia a HDF")
adj_matrix.to_hdf(path3,key='table', comp='blosc')

print(adj_matrix.head())
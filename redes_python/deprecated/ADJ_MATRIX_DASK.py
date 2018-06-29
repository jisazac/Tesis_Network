
from redes_python.utils import metrica_scalar
import pandas as pd
import os




print ("Se importaron las librerias necesarias")


os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","CORR_MATRIX.hdf")


print ("Importando los datos")
df = pd.read_hdf(path, key='table')


names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

from dask import dataframe as dd
from dask.multiprocessing import get
from multiprocessing import cpu_count
nCores = cpu_count()


m=dd.from_pandas(df,npartitions=nCores).\
   map_partitions(
      lambda df : df.apply(
         lambda x : metrica_scalar(x),axis=0)).\
   compute(get=get)




if __name__ == '__main__':
    print(nCores)
    print(m.head())
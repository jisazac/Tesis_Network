"""
Este codigo toma el hdf con los precios, calcula los retornos y
calcula unos vectors de edges para ahorrar espacio, aplica la transformacion de Bonanno
y la exporta en formato hdf y formato csv
"""
from redes_python.utils import metrica_scalar
import pandas as pd
import os
import numpy as np
print ("Se importaron las librerias necesarias")

threshold=0.5

years=[2016,2017]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Sept","Oct","Nov","Dic"]
indexes_2=["RUSSELL_3000_","SP_500_","FTSE_100_"]
os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
for year in years:
    for i in range(len(meses)):
        path = os.path.join("RAW", indexes_2[2]+str(meses[i])+"_"+str(year)+".hdf")
        print("Importando los datos")
        df = pd.read_hdf(path, key='table')
        print("Calculando retornos")
        df3 = df.pct_change(periods=1)
        print("Calculando la matriz de correlacion")
        corr_matrix = df3.corr()
        print("Eliminando info sobrante")
        corr_matrix = corr_matrix.replace(float(1.0), np.nan)
        corr_matrix = corr_matrix.mask(np.arange(corr_matrix.shape[0])[:, None] >= np.arange(corr_matrix.shape[0]))
        corr_matrix[ ( corr_matrix>= -threshold) & (corr_matrix <= threshold)] = np.nan
        print("Eliminando celdas missing")
        edges_df = corr_matrix.stack().reset_index()
        edges_df.columns = ["Source", "Target", "Weight"]
        edges_df=edges_df.round(2)
        edges_df=edges_df.applymap(metrica_scalar)
        # corr_matrix=corr_matrix.cut(corr_matrix.columns,bins=[-0.1,0.1],labe)
        path2 = os.path.join("PROCESSED", "ADJ_LIST_"+indexes_2[2]+str(meses[i])+"_"+str(year)+".csv")
        path3 = os.path.join("PROCESSED", "ADJ_LIST_"+indexes_2[2]+str(meses[i])+"_"+str(year)+".hdf")
        print("Exportando vector correlacion a HDF"+str(meses[i])+str(year))
        edges_df.to_hdf(path3, key='table', comp='blosc')
        print("Exportando vector de correlacion a CSV" + str(meses[i]) + str(year))
        edges_df.to_csv(path2, header=["Source", "Target", "Weight"], chunksize=100, index=False)
        print("-------------------------------------------------------")

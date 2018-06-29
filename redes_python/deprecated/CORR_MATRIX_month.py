"""
Este codigo toma el hdf con los precios, calcula los retornos y
calcula una matriz de correlacion 3000x3000, y la exporta en formato hdf y formato csv
No aplica ninguna transformacion adicional a los datos

"""

import pandas as pd
import os
import numpy as np
print ("Se importaron las librerias necesarias")

n_stocks=3000
threshold=0.4


years=[2016,2017]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Sept","Oct","Nov","Dic"]
indexes_2=["RUSSELL_3000_","SP_500_"]
os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
for year in years:
    for i in range(len(meses)):
        path = os.path.join("RAW", indexes_2[1]+str(meses[i])+"_"+str(year)+".hdf")
        print("Importando los datos")
        df = pd.read_hdf(path, key='table')
        print("Modificando el tamano del dataframe")
        df2 = df.iloc[:, 0:n_stocks]
        print("Calculando retornos")
        df3 = df2.pct_change(periods=1)
        print("Calculando la matriz de correlacion")
        corr_matrix = df3.corr()
        corr_matrix = corr_matrix.replace(float(1.0), np.nan)
        corr_matrix = corr_matrix.mask(np.arange(corr_matrix.shape[0])[:, None] >= np.arange(corr_matrix.shape[0]))
        corr_matrix[(corr_matrix >= -threshold) & (corr_matrix <= threshold)] = np.nan
        # corr_matrix=corr_matrix.cut(corr_matrix.columns,bins=[-0.1,0.1],labe)
        path2 = os.path.join("RAW", "CORR_MATRIX.csv")
        path3 = os.path.join("RAW", "CORR_MATRIX_"+indexes_2[1]+str(meses[i])+"_"+str(year)+".hdf")
        print("Exportando matriz de correlacion a HDF"+str(meses[i])+str(year))
        corr_matrix.to_hdf(path3, key='table', comp='blosc')






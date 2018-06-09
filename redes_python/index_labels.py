
"""
Este script toma el excel que lanza bloomberg con todos los activos y su sector,  luego exporta los datos en formato csv
"""
import pandas as pd
import numpy as np
import os

indexes_1=["RUSSELL_3000_LABELS.xlsx","SP_500_LABELS.xlsx"]
os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW",indexes_1[1])
df=pd.read_excel(path)
indexes_2=["RUSSELL_3000_labels.csv","SP_500_labels.csv"]
path2=os.path.join("RAW",indexes_2[1])
df.to_csv(path2,index=False,chunksize=100)
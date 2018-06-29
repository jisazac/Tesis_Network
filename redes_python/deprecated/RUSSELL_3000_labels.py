"""
Este script toma el excel que lanza bloomberg con todos los activos y su sector,  luego exporta los datos en formato csv
"""
import pandas as pd
import numpy as np
import os

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000_LABELS.xlsx")
df=pd.read_excel(path)

path2=os.path.join("RAW","RUSSELL_3000_labels.csv")
df.to_csv(path2,index=False,chunksize=100)
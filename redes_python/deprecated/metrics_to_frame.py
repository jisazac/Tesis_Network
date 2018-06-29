"""
Este codigo toma el hdf con la lista de edges stacked para un unico mes
calcula metricas de la red, y retorna el dataframe, luego lo exporta en formato csv con miras al panel data
"""

import pandas as pd
import os
import numpy as np
import networkx as nx
print ("Se importaron las librerias necesarias")

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("PROCESSED","ADJ_LIST_RUSSELL_3000_Enero_2016.hdf")
print("Importando los datos")
edges_df = pd.read_hdf(path, key='table')


print("Definiendo la red")
G = nx.from_pandas_dataframe(edges_df, 'Source', 'Target', 'Weight')


print("Calculando Metricas")
df=pd.DataFrame(nx.degree_centrality(G).items(), columns=["stock","Centrality"])  #list(d.items())
df["Closeness"]=nx.closeness_centrality(G).values()
df["Betweenness"]=nx.betweenness_centrality(G).values()
df["Eigenvector"]=nx.eigenvector_centrality(G).values()

if __name__ == '__main__':
    print(df)


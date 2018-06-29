"""
Este codigo toma el hdf con la lista de edges stacked para todos los meses
calcula metricas de la red, y retorna el dataframe, luego lo exporta en formato csv con miras al panel data para
cada indice
"""


import pandas as pd
import os
import networkx as nx
print ("Se importaron las librerias necesarias")



years=[2016,2017]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Sept","Oct","Nov","Dic"]
indexes_2=["RUSSELL_3000_","SP_500_","FTSE_100_","IBOV_","TSWE_"]

index_to_use=indexes_2[4]

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
for year in years:
    for i in range(len(meses)):
        #"ADJ_LIST_RUSSELL_3000_Enero_2016.hdf"
        path = os.path.join("PROCESSED", "ADJ_LIST_"+index_to_use+str(meses[i])+"_"+str(year)+".hdf")
        print("Importando los datos")
        edges_df = pd.read_hdf(path, key='table')
        print("Definiendo la red")
        G = nx.from_pandas_dataframe(edges_df, 'Source', 'Target', 'Weight')
        print("Calculando Metricas")
        df = pd.DataFrame(nx.degree_centrality(G).items(), columns=["stock", "Centrality"])  # list(d.items())
        df["Closeness"] = nx.closeness_centrality(G).values()
        df["Betweenness"] = nx.betweenness_centrality(G).values()
        df["Eigenvector"] = nx.eigenvector_centrality(G).values()
        print("Exportando metricas de la red a CSV" + str(meses[i]) + str(year)+" "+index_to_use)
        path2 = os.path.join("PROCESSED", index_to_use + str(meses[i]) + "_" + str(year) + "_m.csv")
        df.to_csv(path2, header=df.columns, chunksize=100, index=False)
        print("-------------------------------------------------------")


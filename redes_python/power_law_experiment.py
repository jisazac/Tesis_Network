"""
Este codigo toma el hdf con los precios, calcula los retornos y
calcula una matriz de correlacion para el SP500, y la exporta en formato hdf y formato csv
Luego, aplica el programa power law para ver si el fit es adecuado

"""
import networkx as nx
import pandas as pd
import os
import numpy as np
import powerlaw

print ("Se importaron las librerias necesarias")


indexes=["SP_500.hdf","FTSE_100.hdf","TSWE.hdf"]

n_stocks=3000
threshold=0.3

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW",indexes[0])


print ("Importando los datos")
df = pd.read_hdf(path, key='table')



names=[]
for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names

#print ("Modificando el tamano del dataframe")
#df2=df.iloc[:,0:n_stocks]

print ("Calculando retornos")
df2=df.pct_change(periods=1)

print ("Calculando la matriz de correlacion")
corr_matrix=df2.corr()
#corr_matrix=corr_matrix.replace(float(1.0),np.nan)
corr_matrix.values[[np.arange(len(corr_matrix))]*2] = np.nan
corr_matrix = corr_matrix.mask(np.arange(corr_matrix.shape[0])[:, None] >= np.arange(corr_matrix.shape[0]))
for i in range(2,10,1):
    corr_matrix[( corr_matrix>= -(i/10.0)) & (corr_matrix <= (i/10.0))] = np.nan

    edges_df=corr_matrix.stack().reset_index()
    edges_df.columns=["Source", "Target","Weight"]
    G = nx.from_pandas_dataframe(edges_df, 'Source', 'Target', 'Weight')
    degree=G.degree()
    x_values=sorted(set(degree.values()))
    y_values=[degree.values().count(x) for x in x_values]

    print("rho", i / 10.0)
    print("x-axis", x_values)
    print("y-axis", y_values)
    #log_values=map(np.log,values )
    #log_hist = map(np.log, hist)
    #x=np.asarray(log_values,float)
    #y=np.asarray(log_hist, float)

    fit=powerlaw.Fit(y_values,discrete=True)

    print("x_min",fit.xmin)
    print("x_max", fit.xmax)
    print("alpha",fit.power_law.alpha)
    print("D",fit.power_law.D)
    R, p = fit.distribution_compare("power_law", "exponential", normalized_ratio = True)
    # R is the loglikelihood ratio between the two candidate distributions. This number will be positive
    # if the data is more likely in the first distribution, and negative if the data is more likely in the second
    # distribution. The significance value for that direction is p.
    print (R, "positive is good")
    print(p,"p-value")
    print ("")
    print("--------------------------------------------------------------------------------------")



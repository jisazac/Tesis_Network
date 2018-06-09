"""
Este codigo toma el hdf con los precios, calcula los retornos y
calcula una matriz de correlacion para el SP500, y la exporta en formato hdf y formato csv
No aplica ninguna transformacion adicional a los datos

"""
import networkx as nx
import pandas as pd
import os
import numpy as np
import collections
from scipy import stats
import matplotlib.pyplot as plt
print ("Se importaron las librerias necesarias")


indexes=["RUSSELL_3000.hdf","SP_500.hdf","FTSE_100.hdf"]

n_stocks=3000
threshold=0.3

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW",indexes[2])


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
#degree=nx.degree(G)
#corr_matrix[( corr_matrix>= -threshold) & (corr_matrix <= threshold)] = np.nan
#degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
#degreeCount = collections.Counter(degree_sequence)
#deg, cnt = zip(*degreeCount.items())

    degree=G.degree()
    values=sorted(set(degree.values()))
    hist=[degree.values().count(x) for x in values]
    log_values=map(np.log,values )
    log_hist = map(np.log, hist)
    x=np.asarray(log_values,float)
    y=np.asarray(log_hist, float)
    print("valores mayores a "+"0."+str(i))
    print "x-degree",(values)
    print "y- Number of nodes", (hist)

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print "r-squared:", r_value ** 2
    print "slope:",slope
    print "Intercept:", intercept
    print "predicted", p_value
    print""
    k=slope
    R_squared=r_value ** 2
    plt.figure(figsize=(12, 9))
    ax = plt.subplot(111)
    ax.plot(log_values,log_hist,'ro') # in-degree
    ax.plot(x, intercept + slope * x, 'navy', label='fitted line', linewidth=2)  # predicted

    #RIGHT LONG TAIL, TO THE LEFT THE FEW THAT DOMINE
    #ax.legend('degree')
    ax.set_xlabel('Log-Degree', fontsize=16)
    ax.set_ylabel('Log-Nodes', fontsize=16)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim([0, 4])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax.set_title('Distribution '+str(indexes[2][0:-4])+" "+r'$\rho > $'+str(float(i/10.0)))
    props = dict(boxstyle='round', facecolor='gray', alpha=0.5)
    textstr = '$\mathrm{k}=%.2f$\n$\mathrm{R^{2}}=%.2f$\n$\mathrm{intercept}=%.2f$' % (k, R_squared, intercept)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,verticalalignment='top', bbox=props)
    plt.savefig("foo" + str(i) + ".png")
    plt.show()







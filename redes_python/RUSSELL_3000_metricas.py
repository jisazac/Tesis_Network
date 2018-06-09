"""
Este codigo toma el csv con la natriz de correlaciones y le aplica calculos y extrae graficas


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import os


print ("Se importaron las librerias necesarias")

n_stocks=3000
corr_cut=0.9
z=int(n_stocks*(n_stocks-1)/2)


os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000_corr.csv")
df=pd.read_csv(path)
print ("Se importo al dataframe")

df2=df.iloc[0:n_stocks,0:n_stocks+1]
print ("Se modifico el tamaño del dataframe")
m=df2.iloc[0:,1:].as_matrix()
m[np.arange(m.shape[0])[:, None] >= np.arange(m.shape[1])] = np.nan
A = m.flatten()
data=[]
for i in range(z):
    data.append(A[i])
data2 = [x for x in data if str(x) != 'nan']
if __name__ == '__main__':
    # Common sizes: (10, 7.5) and (12, 9)
    plt.figure(figsize=(12, 9))
    # Remove the plot frame lines. They are unnecessary chartjunk.
    ax = plt.subplot(111)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    # Make sure your axis ticks are large enough to be easily read.
    # You don't want your viewers squinting to read your plot.
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    # Along the same vein, make sure your axis labels are large
    # enough to be easily read as well. Make them slightly larger
    # than your axis tick labels so they stand out.
    plt.xlabel("rho", fontsize=16)
    plt.ylabel("P(rho)", fontsize=16)
    # Plot the histogram. Note that all I'm passing here is a list of numbers.
    # matplotlib automatically counts and bins the frequencies for us.
    # "#3F5D7D" is the nice dark blue color.
    # Make sure the data is sorted into enough bins so you can see the distribution.
    #plt.hist(data2,  color="#3F5D7D", bins=100)
    ax.hist(data2,color="#3F5D7D", bins=100, weights=np.zeros_like(data2) + 1. / len(data2))
    plt.show()


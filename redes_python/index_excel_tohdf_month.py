"""
Este codigo toma el excel que lanza bloomberg con todos los activos y convierte el dataframe a
formato hdf, primer codigo en correr


"""

import pandas as pd
import os
import collections
print ("Se importaron las librerias necesarias")

n_stocks=3000
indexes_1=["RUSSELL_3000.xlsx","SP_500.xlsx","FTSE_100.xlsx"]
indexes_2=["RUSSELL_3000_","SP_500_","FTSE_100_"]
mes_2016={"Enero":[1,21],"Febrero":[22,42],"Marzo":[43,65],"Abril":[66,86],"Mayo":[87,108],"Junio":[109,130],
            "Julio":[131,151],"Agosto":[152,174],"Sept":[175,196],"Oct":[197,217],"Nov":[218,239],"Dic":[240,261]
                    }

v_2016=[[1,21],[22,42],[43,65],[66,86],[87,108],[109,130],
            [131,151],[152,174],[175,196],[197,217],[218,239],[240,261]]

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Sept","Oct","Nov","Dic"]

v_2017=[[262,283],[284,303],[304,326],[327,346],[87,108],[109,130],
            [131,151],[152,174],[175,196],[197,217],[218,239],[240,261]]


os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW",indexes_1[2])
df=pd.read_excel(path)
print ("Se importo al dataframe")



df=df.set_index("index")


for i in range(len(meses)):
    names = []
    l= v_2016[i][0]
    u= v_2016[i][1]
    #print(l,u,meses[i])
    df2 = df.iloc[l-1:u, 0:n_stocks]
    df2=df2.set_index("Dates")
    for j in range(len(list(df2))):
        z = df2.columns[j].split()
        names.append(z[0])
    df2.columns=names

    path2 = os.path.join("RAW", indexes_2[2]+str(meses[i])+"_2016"+".hdf")
    print("Exportando la base HDF 2016"+" "+str(meses[i]))
    df2.to_hdf(path2, key="table", comp="blosc")

for i in range(len(meses)):
    names = []
    l= v_2017[i][0]
    u= v_2017[i][1]
    #print(l,u,meses[i])
    df2 = df.iloc[l-1:u, 0:n_stocks]
    df2=df2.set_index("Dates")
    for j in range(len(list(df2))):
        z = df2.columns[j].split()
        names.append(z[0])
    df2.columns=names

    path2 = os.path.join("RAW", indexes_2[2]+str(meses[i])+"_2017"+".hdf")
    print("Exportando la base HDF 2017"+" "+str(meses[i]))
    df2.to_hdf(path2, key="table", comp="blosc")
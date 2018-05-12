"""
Este codigo toma el excel que lanza bloomberg con todos los activos y convierte el dataframe a
formato hdf, primer codigo en correr


"""

import pandas as pd
import os
print ("Se importaron las librerias necesarias")

mes_2016={"Enero":[1,21],"Febrero":[22,42],"Marzo":[43,65],"Abril":[66,86],"Mayo":[87,108],"Junio":[109,130],
            "Julio":[131,151],"Agosto":[152,174],"Sept":[175.196],"Oct":[197,217],"Nov":[218,239],"Dic":[240,261]
                    }

mes_2017={"Enero":[262,283],"Febrero":[284,303],"Marzo":[304,326],"Abril":[327,346],"Mayo":[87,108],"Junio":[109,130],
            "Julio":[131,151],"Agosto":[152,174],"Sept":[175.196],"Oct":[197,217],"Nov":[218,239],"Dic":[240,261]
                    }

os.chdir(u"C:\\Users\\usuario\\Desktop\\Maestr\xedas\\Maestria finanzas eafit\\Tesis_Network\\data")
path=os.path.join("RAW","RUSSELL_3000.xlsx")
df=pd.read_excel(path)
print ("Se importo al dataframe")


names=[]
df=df.set_index("Dates")

for i in range(len(list(df))):
    z=df.columns[i].split()
    names.append(z[0])
df.columns=names


path2=os.path.join("RAW","RUSSELL_3000.hdf")

# HDF
print ("Exportando la base HDF")
df.to_hdf(path2,key="table",comp="blosc")
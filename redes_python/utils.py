"""
Este archivo utils.py contiene funciones a utilizar a lo largo de la
tesis
"""
import numpy as np



def metrica_scalar(rho):
    """

    :param rho : Correlacion calculada para cada relacion, pertence al intervalo [-1,1]
    :return: m: Metrica obtenida

    """
    if isinstance(rho,int) or isinstance(rho,float):
        m=(4.0-np.sqrt(8*(1.0-float(rho))))
        return round(m,2)
    else:
        return rho

def filtro_edge(corr_df,threshold=0.1):
    """

    :param weight: Es el peso asigando a cada arista
    :return: w: El mismo valor o np.nan si el valor es filtrado
    """
    low=-1.0*threshold
    #cond1=corr_df[corr_df < threshold]
    #cond2=corr_df[corr_df > low]
    #corr_filt=corr_df[cond1 & cond2]
    cond3=corr_df[corr_df>low] & corr_df[corr_df<threshold]
    corr_df[cond3] = np.nan
    return corr_df


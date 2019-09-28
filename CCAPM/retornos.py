import numpy as np

def retorno(a):
    retornos = a
    retornos = retornos.iloc[:,1:3]
    retornos = np.log( retornos / retornos.shift(1) )
    retornos['CDI'] = a['CDI']
    retornos = retornos.dropna()
    return retornos
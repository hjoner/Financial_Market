def retornos_log(a):
    retornos = a
    retornos = np.log( retornos / retornos.shift(1) )
    retornos = retornos.dropna()
    return retornos
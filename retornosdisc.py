def retornos_disc(a):
    retornos = a
    retornos = ( retornos / retornos.shift(1) ) -1
    retornos = retornos.dropna()
    return retornos
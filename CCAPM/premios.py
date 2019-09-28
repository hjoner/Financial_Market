def premios(a):
    a['PREMIO_GGBR'] = a['GGBR'] - a['CDI']
    a['PREMIO_CONSUMO'] = a['CONSUMO'] - a['CDI'] 
    return a
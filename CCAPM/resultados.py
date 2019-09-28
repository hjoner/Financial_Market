import pandas as pd
from parametros import constante
from parametros import beta1

def resultados(a):
    resultado = {'Constante' : [0], 'Beta1': [0]}
    resultado = pd.DataFrame(resultado)
    resultado['Constante'] = constante(a)
    resultado['Beta1'] = beta1(a)
    print(resultado)
    return resultado.to_csv('resultados.csv')
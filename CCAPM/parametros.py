import statsmodels.api as sm
import pandas as pd

def constante(a):
    X = a['PREMIO_CONSUMO']
    Y = a['PREMIO_GGBR']

    X1 = sm.add_constant(X)
    reg = sm.OLS(Y, X1).fit()

    constante = pd.DataFrame(reg.params)
    constante = constante.iloc[0][0]
    return constante

def beta1(a):
    X = a['PREMIO_CONSUMO']
    Y = a['PREMIO_GGBR']

    X1 = sm.add_constant(X)
    reg = sm.OLS(Y, X1).fit()

    beta = pd.DataFrame(reg.params)
    beta = beta.iloc[1][0]
    return beta

    
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D


def graph1(a):
    df = a


    x = df.iloc[:,0]
    y1 = df.iloc[:,2]
    y2 = df.iloc[:,1]

    fig, ax1 = plt.subplots(1,1,figsize=(15,5), dpi= 60)
    ax1.plot(x, y1, color='tab:red')

    ax2 = ax1.twinx() 
    ax2.plot(x, y2, color='tab:blue')

    ax1.set_xlabel('Trimestres', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=9)
    ax1.set_ylabel('GGBR', color='tab:red', fontsize=20)
    ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
    ax1.grid(alpha=.4)
    ax1.set_facecolor('xkcd:ivory')

    ax2.set_ylabel("CONSUMO", color='tab:blue', fontsize=20)
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    ax2.set_title("GGBR vs CONSUMO ", fontsize=24)
    fig.tight_layout()
    plt.show()
    
    


def graph2(a):
    retornos = a
    X = retornos[['CONSUMO', 'CDI']]
    y = retornos['GGBR']

    X = sm.add_constant(X)
    est = sm.OLS(y, X).fit()


    xx1, xx2 = np.meshgrid(np.linspace(X.CONSUMO.min(), X.CONSUMO.max(), 100), 
                       np.linspace(X.CDI.min(), X.CDI.max(), 100))

    Z = est.params[0] + est.params[1] * xx1 + est.params[2] * xx2

    fig = plt.figure(figsize=(12, 8))
    ax = Axes3D(fig, azim=-115, elev=15)


    surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)

    resid = y - est.predict(X)
    ax.scatter(X[resid >= 0].CONSUMO, X[resid >= 0].CDI, y[resid >= 0], color='black', alpha=1.0, facecolor='white')
    ax.scatter(X[resid < 0].CONSUMO, X[resid < 0].CDI, y[resid < 0], color='black', alpha=1.0)


    ax.set_xlabel('CONSUMO')
    ax.set_ylabel('CDI')
    ax.set_zlabel('GGBR')

    plt.title('RELAÇÃO GGBR - CONSUMO - CDI', fontsize = 20)
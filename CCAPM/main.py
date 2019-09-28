import pandas as pd

# Importando base de dados
dados = pd.read_csv('trimestral.csv')

# Captando a função graph1 do módulo graficos
from graficos import graph1

#Aplicação da função graph1
graph1(dados)

#Aplicando a função retorno criada no módulo retornos
from retornos import retorno
dados = retorno(dados)

# Verificando os prêmios com o módulo premios
from premios import premios
dados = premios(dados)

# Identificando os parâmetros através do módulo parametros
from parametros import constante
print(constante(dados))

from parametros import beta1
print(beta1(dados))

# Visualizando outro gráfico do módulo graficos
from graficos import graph2
graph2(dados)

# Exportanto os resultados através do módulo resultados
from resultados import resultados
resultados(dados)
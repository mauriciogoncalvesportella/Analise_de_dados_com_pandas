# carregando os dados do arquivo Excel

import pandas as pd
import plotly_express as px

# fazendo a leitura dos dados (nesse código, o arquivo Excel precisa estar na mesma pasta)

caminho_arquivo = r"C:\Users\mauro\OneDrive\Área de Trabalho\Python\Empowerdata\Aula 3\Aula 3 - VIP\vendas.xlsx"
dados = pd.read_excel(caminho_arquivo)
print(dados.head())
# criando um gráfico de barras com base nos dados da tabela "Dados"

# Análise exploratória = verificando se os dados foram carregados corretamente

# head(): mostra as primeiras linhas do conjunto de dados
# tail(): mostra as últimas linhas do conjunto de dados

# shape verifica a quantidade de linhas e colunas. O primeiro valor é a quantidade de linhas e o segundo a de colunas

print(dados.shape)

print(dados.info)

# Gerador de estatísticas sobre todas as colunas quantitativas

print(dados.describe)

#Acessando uma coluna específica

print(dados["loja"])

print(dados.loja)

# Para obter os valores únicos de uma coluna, ultilizamos o método unique()

print(dados["loja"].unique())

# Fazendo contagem de valores de uma coluna, ou também buscar o valor relativo

print(dados["loja"].value_counts)
print(dados["loja"].value_counts(normalize=True))

# Agrupamento de dados por determinada coluna

print(dados.groupby("loja").preco.sum())
print(dados.groupby("loja").preco.mean())
print(dados.groupby("loja").preco.std())
print(dados.groupby("loja").preco.var())


# Gráficos

print(px.histogram(dados, x="loja", color="regiao", text_auto=True))

# Criando múltiplos gráficos

colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in colunas:
    fig = px.histogram(dados, x="loja", color="regiao", text_auto=True)
    fig.show()
    fig.update_layout(title={"text": f'Histograma - {coluna}'}, autosize=False,width=1000, height=800)



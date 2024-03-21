import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import seaborn as sns
import yaml

# Carregar dados do arquivo YAML
with open("Desafio/EmpresaBanheira/empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Criar DataFrame com os dados
df = pd.DataFrame(dados["vendas"])

# Mostando a tabela
print(df)


# Plotando gráfico de contagem de vendas X Mês

# Encontrando o Mês de cada
df["month"] = pd.DatetimeIndex(df["data"]).month
print(df["month"])

# Calculando a contagem
contagemVendas = df["month"].value_counts()
print(f"A contagem é {contagemVendas}")


# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
graficoContMe = plt.bar(contagemVendas.index, contagemVendas.values, width = 0.5, align='center')
plt.title('Vendas X Mês')  # Definir título do gráfico
plt.xlabel('Mês')  # Definir rótulo do eixo x
plt.ylabel('Contagem de Vendas')  # Definir rótulo do eixo y

plt.bar_label(graficoContMe, fmt="%.01f", label_type="edge")  # Mostrar o gráfico
plt.show()

# Media de itens vendidos por Venda

# Media de itens vendidos
media_itens_vendidos = df["quantidade"].mean()

print(media_itens_vendidos)




# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
graficotes = plt.bar(media_itens_vendidos, df['produto'], width = 0.5, align='center')
plt.title('Vendas X Mês')  # Definir título do gráfico
plt.xlabel('Mês')  # Definir rótulo do eixo x
plt.ylabel('Contagem de Vendas')  # Definir rótulo do eixo y

plt.bar_label(graficotes, fmt="%.01f", label_type="edge")  # Mostrar o gráfico
plt.show()



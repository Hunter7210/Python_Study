import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_excel('Plotagem/filmes.xlsx')

# Verificar as primeiras linhas do DataFrame para garantir que as colunas estão presentes
print(df.head())

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(df['Nome'], df['Avaliacao'], color='purple')
plt.xlabel('Nome')
plt.ylabel('Avaliacao')
plt.title('Receita por Filme')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Calcular a contagem de filmes por gênero
contagem_por_genero = df['Gênero'].value_counts()


# Definir paleta de cores
cores = sns.color_palette('pastel')[:5]

# Plotar o gráfico de pizza
plt.figure(figsize=(5, 5))
plt.pie(contagem_por_genero, labels=contagem_por_genero.index, colors=cores, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição dos Filmes por Gênero')
plt.axis('equal')  # Mantém a proporção do gráfico para que seja um círculo
plt.show()

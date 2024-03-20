import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml


# Carregar dados do arquivo YAML
with open('Desafio/EmpresaBanheira/empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Ler conjunto de dados em DataFrame Pandas
# Verificar o comprimento de cada coluna
for key, value in dados.items():
    print(f"Comprimento da coluna '{key}': {len(value)}")
    
# Criar DataFrame com os dados
df = pd.DataFrame(dados)



# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.hist(df['idade'], bins=5, color='skyblue', edgecolor='black')  # Plotar histograma
plt.title('Histograma da Idade - Matplotlib')  # Definir título do gráfico
plt.xlabel('Idade')  # Definir rótulo do eixo x
plt.ylabel('Frequência')  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico

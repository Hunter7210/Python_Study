#Posições
#Posições Vencedoras
#Preencher os campos
#Verificar se ganhou
#Alternar entre jogadores
#Preencher os campos
#Verificar se ganhou
#Pontuar



#Posições
#Posições vencedoras
#Exibir tabuleiro

# Importar bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns

# Definir dados
dados = [40, 60] # Valores de X e O
rotulos = ['X', 'O'] # Rótulos de X e O

# Definir paleta de cores
cores = sns.color_palette('pastel')[:2]

# Criar gráfico de pizza
plt.pie(dados, labels=rotulos, colors=cores, autopct='%1.1f%%')
plt.title('Gráfico de pizza de x e O')
plt.show()


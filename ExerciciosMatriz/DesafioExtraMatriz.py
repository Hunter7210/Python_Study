from turtle import color
from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])
# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50   # Exemplo:o investidor possui 50 ações da Ação 2
# Calculando o valor do investimento em cada dia

investim_diario_acao1 = acoes_acao1 * preco_medio_acao1

investim_diario_acao2 = acoes_acao2 * preco_medio_acao2

print(investim_diario_acao1, investim_diario_acao2)
# Calculando o patrimônio total do investidor em cada dia
patrimo_invest = investim_diario_acao1 + investim_diario_acao2

print(patrimo_invest)

cont = 1

# Exibindo os resultados diariamente
for i in patrimo_invest:
    print(f"Dia{cont}: {i}")
    cont+=1

array_dia = np.array([1,2,3,4,5,6,7,8,9,10])
#plot o gráfico da evolução patrimonial do investidor
plt.title('Grafico de investimento')
plt.plot(array_dia, patrimo_invest , marker='o', color='b')
plt.plot(array_dia, investim_diario_acao1, marker='o', color='r')
plt.plot(array_dia, investim_diario_acao2, marker='o', color='g')
plt.ylabel('Patrimônio')
plt.xlabel('Ações')
plt.grid('true')

plt.show()



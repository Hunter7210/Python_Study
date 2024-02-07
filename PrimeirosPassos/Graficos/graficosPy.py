import matplotlib.pyplot as plt

# Criando um gráfico simples
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]
z = [3, 5, 27, 2, 48]

pfig = plt.figure()
ax = plt.axes(projection='3d')

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exemplo de Gráfico')
plt.show()


#Antes de executar é importante instalar a biblioteca do matplotlib execute no terminal o seguinte comando py -m pip install matplotlib


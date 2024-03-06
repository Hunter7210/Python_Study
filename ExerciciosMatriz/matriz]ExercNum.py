import numpy as np #Necessário instalar as dependencias do numpy pelo console: py -m pip install numpy #pip é um gerenciador de dependencias

empty_array = np.empty((3, 3)) #Criando uma matriz vazia com 3 linhas e 3 colunas
print(empty_array)

#Criação de um array 2,2 preenchido com numeros 1
ones_array = np.ones((2, 2))
print(ones_array)

#Criando uma matriz nula, onde todos os elementos são 0
zeros_array = np.zeros((4, 4))
print(zeros_array)

#Criando um array 3,3 com numeros aleatorios
random_array = np.random.rand(3, 3) #Random já esta dentro da biblioteca do NUMPY
print(random_array)


#Indexação e Seleção de elementos:

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
#Na indexação dele começa com 0, diferentemente da matematica onde começa por 1 
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6), pois o indice começa com 0

#Encontrar o máximo e o mínimo em uma matriz
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

#Calculando a soma dos valores
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")

#Manipulando Arrays:

#Serve para remover aquelas linhas que estão sem valor, nulo, unidimensionais
squeezed_array = np.squeeze(my_array) # Esquece remove, valores nulos
print(squeezed_array)

#Adição de matrizes:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

#Subtração de matrizes:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

#Multiplicação de matrizes:

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

#É IMPORTANTE LEMBRAR QUE PARA REALIZAR ESSES CALCULOS DEVE SER UTILIZADO O ARRAY DO NUMPY COM:  np.array([[]]);



#Operações estátisticas




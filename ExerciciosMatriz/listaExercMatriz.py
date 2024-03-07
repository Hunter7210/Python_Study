from ctypes.wintypes import PINT
import random
import numpy as np 

#Exercicio 01

#Criando uma matriz vazia com 3 linhas e 3 colunas
array_vazio = np.empty((3,3))
print(array_vazio)

#Criação de um array 2,2 preenchido com numeros 1
array_num1 = np.ones((2,2))
print(array_num1)

#Exercicio 02

#Criando uma matriz nula, onde todos os elementos são 0
array_zeros = np.zeros((3,3))
print(array_zeros)

#Exercicio 03

#Criando arrays de numeros aleatórios
np.random.seed(1)
array_tes = np.random.rand(2,2)
print(array_tes)


#Exercicio 04

array_unid = np.array((1,2,3,4,5))

#Exercicio 05

matriz_2x3 = np.random.randint(10, size=(1,2))

# Indexação e Seleção:

#Exercicio 01
array_exem = np.array([[1, 2, 3], [4, 5, 6], [0,0,0]])
print(array_exem[0,0])

#Exercicios 02
num_max = np.max(array_exem)
num_min = np.min(array_exem)
print(f"Numero Max: {num_max}, Numero Min: {num_min}")

#Exercicio 03
#Calculando a soma dos valores
total_sum = np.sum(array_exem)
print(f"Soma total: {total_sum}")

#Manipulação de Arrays

#Exercicio 01
#Serve para remover aquelas linhas que estão sem valor, nulo, unidimensionais
squeezed_array = np.squeeze(array_exem) # Esquece remove, valores nulos
print(squeezed_array)

#Exercicio 02
#Adição de matrizes:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

#Subtração de matrizes:
mat1 = np.array([[3,5], [6,8], [0,9]])
mat2 = np.array([[3,2], [6,5], [3,9]])
result = mat1-mat2 #Lembrando que  mat1-mat2 <> mat2-mat1
print(f"Subtração é: {result}")

#Exercicio 03

#Realizando a multiplicação de matrizes
matri1 = np.array([[1,2],[1,2]])
matri2 = np.array([[3,2],[7,2]])
res = np.dot(matri1, matri2)
print(res)

#Operações Estatísticas

#Exercicio 01

#Calculando a Media de uma matriz plana
media_matriz = np.average(mat1)
print(media_matriz)

#Calculando a mediana de uma matriz plana
sorted_numbers_array = np.sort(mat2) #Ordena o Array em ordem crescente
mediana_matriz = np.median(sorted_numbers_array) #Verifica qual o valo no centro
print(f"Matriz 2 {mat2}")
print(f"Mediana da matriz: {mediana_matriz}") 

#Calculando o desvio padrão de uma matriz plana
desvio_padrao_matriz = np.std(mat1)
print(f"O desvio padrão é: {desvio_padrao_matriz}")

#Exercicio 02

#Soma dos elementos na diagonal
diagonal_sum = np.trace(matri2)
print(f"Soma diagonal: {diagonal_sum}")


#Desafios Avançados

#Exercicio 01
#Encontrando o numero de linhas e colunas de uma matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")


#Exercicio 02
#Verificar se um array contem  uma linha especifica
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_especifica = np.array([4, 5, 6])
contem_linha = np.isin(matriz, linha_especifica).all(axis=1).any()
print(f"Contém a linha específica? {contem_linha}")


#Exercicio 03
#Transpor uma matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = np.transpose(matriz)
# Ou, alternativamente: matriz_transposta = matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)    
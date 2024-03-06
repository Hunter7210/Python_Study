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
array_exem = np.array([1,2,3], [4,5,6])
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

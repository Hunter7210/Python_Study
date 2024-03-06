
#Ativ 1

import random
import statistics
from textwrap import indent

import numpy as np
from seaborn import plotting_context


numeros = [1,2,3,4,5]

print(numeros)

#Ativ 2

numeros = [1,2,3,4,5]

numeros.reverse()

print(numeros)

#Ativ 3

notas = [1,2,3,4,5,6,7,8,9,10]
#Utilizando a biblioteca statitics é possivel realizar diversas contas matematicas
media = statistics.mean(notas)

print(media)


#Ativ 4

chars = ["K","O","E","N","I","G","S","E","G","G"]
vogais = ["A","E","I","O","U"]

cont = 0

for i in chars:
    for j in vogais:
        if i == j:
            cont += 1
print(f"Seu vetor tem {cont} consoantes")

#Ativ 5

numbers20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

par =[]
impar=[]

for i in numbers20:
    if (i%2) == 0:
        par.append(i)
    else:
        impar.append(i)

print(numbers20)
print(par)
print(impar)


#Ativ 6 
condicao = 0
while condicao<2:

    aluno = input("Bem vindo, digite aqui o nome do aluno")
    matematica = int(input("Digite aqui as notas de Matematica:"))
    bio = int(input("Digite aqui as notas de Biologia:"))
    fis = int(input("Digite aqui as notas de Fisica:"))
    qui = int(input("Digite aqui as notas de Quimica:"))
    
    soma = int(matematica+bio+fis+qui)
    media_not = soma/4

    notas = [media_not]
    print(media_not)
    print(notas)


    contNotas = 0
    for i in notas:
        if i>=7.0:
            print(f"O aluno {aluno} esta aprovado!") 
            contNotas+=1
        else:
            print(f"O aluno {aluno} esta reprovado!")

    condicao+=1        


#Ativ7
    
num5 = [1,2,3,4,5]

soma = sum(num5)
mult = np.multiply(num5)

print(num5)
print(soma)
print(mult)
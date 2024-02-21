# Criação de Conjuntos:

#Nos conjuntos não pode repetir o mesmo valor, ele não contem indice, muito usada para evitar duplicidade e realizar a união entre dois conjuntos
#É representado por {} 

# Conjunto de números
numeros = {1, 2, 3, 4, 5}

# Conjunto de letras
vogais = {'a', 'e', 'i', 'o', 'u'}

# Operações de Conjuntos:
# União de conjuntos
uniao = numeros.union(vogais)  # Resultado: {1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u'}

# Interseção de conjuntos
intersecao = numeros.intersection({3, 4, 5, 6})  # Resultado: {3, 4, 5}

# Diferença de conjuntos
diferenca = numeros.difference({4, 5, 6})  # Resultado: {1, 2, 3}

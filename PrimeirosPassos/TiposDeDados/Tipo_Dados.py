#Tipos de variaveis
# int, str, float ,bool, list, tuple, dict

# Para converter um valor utiliza o Casting
# numero = 42
# texto = str(numero)  # Converte o número para string


# INT
num1 = 1
num2 = 3

# FLOAT
num1 = 2.3
pi = 3,14

# STRING
text1 = "Heitor"

# Boolean
ligado = True
desligado = False

# Listas e Tupla 
# Lista(Array que aumenta)
# Tupla(Não aumenta)

# Listas Utilizam COLCHETES[]
frutas = ["maçã, banana, uva"]
numeros = [1,2,3,4,5]

# Adicionando elementos
frutas.append("Laranja")
print(frutas)

# Imprimir um valor especifico utilizar o index 
print(frutas[1])

# Tuplas utilizam PARENTESÊS()
coordenadas = (4,5)
cores_rgb = (255,0,0)

print(coordenadas)

print(coordenadas[1])

# O dicinario funciona fazendo a busca de um valor chave e me retornando o valor desta chave EX: Chamei a palavra-chave nome ele me retorná Carlos;
# Dicionario chave valor
pessoa = {
    "nome": "Carlos",
    "idade": "30",
    "profissao": "engenheiro"

}

# Acessando valores, não é necessário utilizar o .get
print(pessoa["nome"])
print(pessoa.get("idade"))


# Adicionando novo par chave-valor
pessoa["cidade"] = "São Paulo"
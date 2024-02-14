# 1
from matplotlib import axes

print("Digite o primeiro valor")
a = int(input())

print("Digite o segundo valor")
b = int(input())


print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

# Declare uma variável para representar o raio de um círculo e calcule sua área usando a fórmula área = π * raio^2. Considere π como 3.14.
pi = 3.14
calculo = pi * float(a**2)
print(f"O raio do seu circulo é: {calculo}")

# 2
nome = "Heitor"
sobrenome = "Rodrigo"

nome_completo = nome + "" + sobrenome

print(nome_completo)

# Frase
frase = "A Pagani é a marca que possui os carros mais bonitos"

# Maiusculas
print(frase.upper())

# Minusculas
print(frase.lower())

# Substituindo uma palavra da frase
print(frase.replace("Pagani", "koenigsegg"))


# Criar lista
cores = ["Azul", "Verde", "Roxo"]

cores.append("Rosa")
cores.append("Nardo")
print(cores)

# Criar uma tupla
longLat = (2, 3)

print(longLat[0])
print(longLat[1])


# Booleanas
tem_sol = True
tem_chuva = False

o_dia_esta_agradavel = not tem_chuva

print(f"O dia esta agradavél? {o_dia_esta_agradavel}")

# Impar ou Par

print("Digite um n°:")
num1 = int(input())

print("Digite outro n°:")
num2 = int(input())

restoNum1 = num1 % 2
restoNum2 = num2 % 2

if restoNum1 and restoNum2 == 0:
    print("Ambos são pares")
else:
    print("Eles não são pares")


# Criar uma lista de numeros
listaNum = [1, 2, 3, 4, 5, 6]
for num in listaNum:
    if num % 3 == 0 and num % 2 != 0:
        print(f"{num} é múltiplo de 3 e ímpar.")
    else:
        print("Não são impares e nem multiplos de 3")

# Idade
idadeUsua = int(input("Digite sua idade:"))

if idadeUsua > 18 and idadeUsua<65:
    print("Você está apito")
else: 
    print("Você não está apito")





# LISTA AVANÇADA

a = float(input("Digiteo coeficiete a: "))
b = float(input("Digiteo coeficiete b: "))
c= float(input("Digiteo coeficiete c: "))

delta = (b**2) - 4*a*c
#raiz quadrada pode ser determinada por tambem por cmath.sqrt (Esta é uma biblioteca que calcula a raiz, é mais pratico pois o metodo normal pode gerar uma Exception, ai tem que tratar
x1 = (-b - (delta**0.5))/2*a
x2 = (-b + (delta**0.5))/2*a

print(x1)
print(x2)


euro = 0.93
libra = 0.80


valorAConvert = float(input("Digite o valor desejado em Dollar:"))

print("Digite para qual moeda você quer converter:")
moedaConvert = int(input("1- euro  2- libra esterlina"))
print(moedaConvert)

if moedaConvert == 1:
    valorConvertEuro = valorAConvert*euro
    print(valorConvertEuro)
else:
    valorConvertLibra = valorAConvert*libra
    print(valorConvertLibra)




fraseAnalisar = input("Digite alguma frase: ")
Palindromo = True

fraseMudada = fraseAnalisar[::-1]
 
if fraseAnalisar == fraseMudada:
    print(Palindromo)
else:
    Palindromo = False
    print(Palindromo)


fraseSeparada = fraseAnalisar.split(' ')

print(fraseAnalisar)

print(len(fraseSeparada))
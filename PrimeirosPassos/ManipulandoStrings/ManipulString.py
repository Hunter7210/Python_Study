# SLICING

# Slicing: O slicing permite extrair partes específicas de uma string.
frase = "Python é uma linguagem poderosa"

# Extrair as primeiras 6 letras
primeiras_letras = frase[:6]

# Extrair as últimas 9 letras
ultimas_letras = frase[-9:]

# Extrair cada duas letra
cada_segunda_letra = frase[::2]

print(primeiras_letras,",", ultimas_letras,"," ,cada_segunda_letra)

# Fomatações avançadas

nome = "João"
idade = 30

# Usando f-strings, passa tudo para str
mensagem = f"Olá, {nome}! Você tem {idade} anos."

# Usando método format
outra_mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)

print(mensagem)
print(outra_mensagem)



# Mais metodos
texto = "   Python é incrível!   "

# Remover espaços em branco no início e no final
texto_trim = texto.strip()

# Converter para letras maiúsculas
texto_upper = texto.upper()

# Converter para letras minusculas
texto_lower = texto.lower()

# Substituir parte do texto, (texto antigo, texto novo)
texto_substituido = texto.replace("Python", "Java")

# Dividir a string em uma lista de palavras
lista_palavras = texto.split()

print(texto_trim)
print(texto_upper)
print(texto_substituido)
print(lista_palavras)


# Verificação e Manipulação:
email = "usuario@email.com"

# Verificar se a string é um e-mail
e_email = email.endswith(".com")

# Contar o número de ocorrências de uma letra
contagem_letra = texto.count("o")

# Encontrar a posição da palavra "incrível"
posicao_incrivel = texto.find("incrível")

print(e_email)
print(contagem_letra)
print(posicao_incrivel)

# Concatenação:
nome = "Maria"
sobrenome = "Silva"

# Concatenar strings usando o operador '+'
nome_completo = nome + " " + sobrenome

# Concatenar usando o método join
lista_palavras = ["Python", "é", "incrível"]
frase_completa = " ".join(lista_palavras) #Acrecenta o " " de acordo com o termino da palavra representado por ","  em cada posição 

print(nome_completo)
print(frase_completa)




#Criação de Dicionários:
# Dicionário de informações sobre uma pessoa


#É possivel criar uma dicionarion onde o resultado da minha chave chamada é um list, tupla etc EX: 
#num = [1,2,3,4]
#pessoa = {'nome': num, 'idade': 25, 'cidade': 'São Paulo'}

pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

# Dicionário vazio
configuracoes = {}

#Acesso a Valores:

# Acesso por chave
nome = pessoa['nome']  # Resultado: 'João'

# Modificação de Valores:

# Modificar um valor
pessoa['idade'] = 26  # Agora o dicionário é {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo'}

# Adição e Remoção de Itens:

# Adicionar novo item
pessoa['profissao'] = 'Engenheiro'  # Resultado: {'nome': 'João', 'idade': 26, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Remover item por chave
del pessoa['cidade']  # Resultado: {'nome': 'João', 'idade': 26, 'profissao': 'Engenheiro'}

import yaml


# Dados iniciais
dados_iniciais = {
    'alunos':['João', 'Maria', 'Pedro', 'Ana', 'Carla', 'Mateus', 'Juliana', 'Lucas', 'Luana', 'Mariana', 'Thiago', 'Camila', 'Fernando', 'Paula', 'Guilherme', 'Bianca', 'Rafael', 'Amanda', 'Diego', 'Isabela', 'Gabriel', 'Letícia', 'Felipe', 'Larissa', 'Matheus', 'Natália', 'Rodrigo', 'Tatiane', 'Vinícius', 'Caroline', 'Daniel', 'Priscila', 'Leandro', 'Lívia', 'Bruno', 'Gabriela', 'Alexandre', 'Vivian', 'Caio', 'Thaís', 'Eduardo', 'Vanessa', 'Gustavo', 'Lara', 'Ricardo', 'Juliana', 'Marcelo', 'Ana Carolina', 'Marina', 'Renato', 'Natasha', 'Henrique', 'Ana Clara', 'Luciana', 'Luciano', 'Patrícia', 'Sandro', 'Jéssica', 'André', 'Bárbara', 'Arthur', 'Priscila', 'Cristiano', 'Monique', 'Felipe', 'Fernanda', 'Diego', 'Tatiane', 'Alex', 'Raquel', 'Junior', 'Jaqueline', 'Rafaela', 'Thiago', 'Bruna', 'Carlos', 'Isabel', 'Paulo', 'Jéssica', 'Renata', 'Vinícius', 'Larissa', 'William', 'Beatriz', 'Marcela', 'Lucas', 'Júlia', 'Marcelo', 'Carolina', 'Renan', 'Silvia', 'Marcelo', 'Thais', 'Raphael', 'Gabriela', 'José', 'Ana Luiza'],
    'notas': [7, 3, 8, 4, 10, 5, 6, 10, 2, 7, 9, 5, 9, 4, 7, 7, 9, 5, 8, 8, 2, 3, 8, 8, 6, 2, 3, 1, 6, 4, 6, 6, 4, 7, 1, 9, 7, 9, 2, 7, 8, 3, 9, 5, 3, 4, 10, 7, 7, 3, 4, 6, 9, 10, 8, 8, 2, 8, 4, 5, 5, 5, 10, 5, 9, 10, 8, 8, 10, 3, 6, 6, 3, 3, 7, 7, 6, 9, 9, 10, 7, 4, 5, 9, 9, 5, 5, 6, 8, 7, 5, 8, 8, 3, 5, 10, 3, 4, 6, 3, 6, 4],
    'idade': [22, 23, 18, 25, 19, 19, 25, 25, 19, 20, 18, 24, 18, 19, 25, 20, 25, 20, 23, 24, 24, 20, 22, 25, 20, 23, 24, 25, 18, 25, 22, 25, 22, 20, 25, 24, 23, 18, 25, 23, 20, 22, 20, 20, 22, 25, 22, 19, 24, 19, 23, 18, 20, 22, 23, 23, 20, 23, 24, 22, 22, 18, 22, 20, 22, 25, 18, 25, 19, 25, 22, 20, 18, 25, 19, 20, 25, 20, 24, 23, 20, 23, 20, 23, 19, 20, 19, 22, 25, 25, 18, 18, 20, 23, 25, 24, 24, 23, 20, 24, 23],
    'altura': [1.85, 1.64, 1.62, 1.72, 1.52, 1.77, 1.71, 1.72, 1.89, 1.86, 1.83, 1.56, 1.67, 1.65, 1.82, 1.68, 1.66, 1.67, 1.53, 1.89, 1.63, 1.68, 1.52, 1.83, 1.77, 1.68, 1.77, 1.55, 1.63, 1.68, 1.66, 1.77, 1.85, 1.89, 1.62, 1.73, 1.55, 1.61, 1.89, 1.65, 1.81, 1.81, 1.69, 1.76, 1.73, 1.77, 1.72, 1.59, 1.68, 1.59, 1.89, 1.75, 1.57, 1.55, 1.67, 1.75, 1.81, 1.53, 1.64, 1.75, 1.78, 1.74, 1.77, 1.77, 1.74, 1.65, 1.81, 1.63, 1.81, 1.69, 1.58, 1.84, 1.88, 1.71, 1.76, 1.89, 1.64, 1.77, 1.72, 1.88, 1.58, 1.68, 1.56, 1.83, 1.66, 1.65, 1.64, 1.88, 1.71, 1.67, 1.68, 1.83, 1.74]

}


# Salvar os dados expandidos em um arquivo YAML
with open('Plotagem/dadosExer.yaml', 'w') as file:
    yaml.dump(dados_iniciais, file)


print("Arquivo YAML com dados expandidos criado com sucesso!")

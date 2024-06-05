#Definições para o programa

import pandas as pd
import plotly.express as px
from flask import Flask, render_template


##Função de Análise de dados
def analise_dados(file_path):
    #Carregar dados so arquivo CSV para um DataFrame do 
    df = pd.read_csv(file_path)

    # Realizar análises básicas (sumário estatístico)
    resumo = df.describe()
    resumo_head = df.head()


    #Gerar graficos interaticos com Ploty
    fig1 = px.histogram(df,x='rating', title='Distribuição das Avaliações dos Filmes')
    fig1.write_html('templates/plot1.html')

    fig2 = px.box(df, x='genre', y='rating', title='Box Plot das Avaliações por Gênero')
    fig2.write_html('templates/plot2.html')
    
    fig3 = px.strip(df, x='votes', y='rating', title='Realação entre votos, Avaliações e Duração dos Filmes')
    fig3.write_html('templates/plot3.html')
    

    return resumo, resumo_head

###Flask setup
## Com flask ele me permite criar um servidor para minhas paginas html, basicamente criação de rotas

app = Flask(__name__)

@app.route('/')
def  index():
    #Analisa os dados e gera os gráficos
    resumo, resumo_head = analise_dados('movies.csv')
    
    #Renderiza o template com o sumário
    return render_template('index.html', resumo = resumo.to_html(), resumo_head = resumo_head.to_html())


@app.route('/plot1')
def plot1():
    return render_template('plot1.html')

@app.route('/plot2')
def plot2():
    return render_template('plot2.html')

@app.route('/plot3')
def plot3():
    return render_template('plot3.html')
    
if __name__ == '__main__' : 
    app.run(debug=True)








